import * as pdfjsLib from "/static/vendor/pdfjs/pdf.mjs";

const ZOOM_STEPS = [0.8, 0.9, 1, 1.1, 1.25, 1.5, 1.75, 2];
const RESIZE_DEBOUNCE_MS = 140;

function isTypingTarget(element) {
    if (!element) {
        return false;
    }
    const tagName = element.tagName;
    return element.isContentEditable || tagName === "INPUT" || tagName === "TEXTAREA" || tagName === "SELECT";
}

function clamp(value, min, max) {
    return Math.max(min, Math.min(max, value));
}

class LessonPdfViewer {
    constructor(root) {
        this.root = root;
        this.frame = root.querySelector(".lesson-pdf-frame");
        this.canvas = root.querySelector(".js-pdf-canvas");
        this.loading = root.querySelector(".js-pdf-loading");
        this.error = root.querySelector(".js-pdf-error");
        this.prevButton = root.querySelector(".js-prev-page");
        this.nextButton = root.querySelector(".js-next-page");
        this.pageInput = root.querySelector(".js-page-input");
        this.pageCount = root.querySelector(".js-page-count");
        this.zoomOutButton = root.querySelector(".js-zoom-out");
        this.zoomInButton = root.querySelector(".js-zoom-in");
        this.fitButton = root.querySelector(".js-fit-page");
        this.fullscreenButton = root.querySelector(".js-fullscreen");

        this.pdfDocument = null;
        this.currentPage = 1;
        this.totalPages = 0;
        this.zoomIndex = ZOOM_STEPS.indexOf(1);
        this.renderTask = null;
        this.renderToken = 0;
        this.resizeTimer = null;
    }

    async init() {
        pdfjsLib.GlobalWorkerOptions.workerSrc = this.root.dataset.workerUrl;
        this.bindEvents();

        if (!document.fullscreenEnabled && this.fullscreenButton) {
            this.fullscreenButton.hidden = true;
        }

        try {
            this.root.classList.add("is-loading");
            this.pdfDocument = await pdfjsLib.getDocument(this.root.dataset.pdfUrl).promise;
            this.totalPages = this.pdfDocument.numPages;
            this.pageCount.textContent = String(this.totalPages);
            this.updateControls();
            await this.renderCurrentPage();
        } catch (error) {
            this.showError();
            console.error("PDF lesson viewer failed to load", error);
        }
    }

    bindEvents() {
        this.prevButton.addEventListener("click", () => this.goToPage(this.currentPage - 1));
        this.nextButton.addEventListener("click", () => this.goToPage(this.currentPage + 1));
        this.zoomOutButton.addEventListener("click", () => this.changeZoom(-1));
        this.zoomInButton.addEventListener("click", () => this.changeZoom(1));
        this.fitButton.addEventListener("click", () => this.resetFit());
        this.pageInput.addEventListener("keydown", (event) => this.handlePageInput(event));
        this.pageInput.addEventListener("blur", () => this.syncPageInput());

        if (this.fullscreenButton) {
            this.fullscreenButton.addEventListener("click", () => this.toggleFullscreen());
        }

        document.addEventListener("keydown", (event) => this.handleKeyboard(event));
        document.addEventListener("fullscreenchange", () => this.handleResize());

        if ("ResizeObserver" in window) {
            this.resizeObserver = new ResizeObserver(() => this.handleResize());
            this.resizeObserver.observe(this.frame);
        } else {
            window.addEventListener("resize", () => this.handleResize());
        }
    }

    async goToPage(pageNumber) {
        if (!this.pdfDocument) {
            return;
        }
        const nextPage = clamp(pageNumber, 1, this.totalPages);
        if (nextPage === this.currentPage) {
            this.syncPageInput();
            return;
        }
        this.currentPage = nextPage;
        this.syncPageInput();
        this.updateControls();
        await this.renderCurrentPage();
    }

    async changeZoom(direction) {
        const nextIndex = clamp(this.zoomIndex + direction, 0, ZOOM_STEPS.length - 1);
        if (nextIndex === this.zoomIndex) {
            return;
        }
        this.zoomIndex = nextIndex;
        this.updateControls();
        await this.renderCurrentPage();
    }

    async resetFit() {
        if (this.zoomIndex === ZOOM_STEPS.indexOf(1)) {
            await this.renderCurrentPage();
            return;
        }
        this.zoomIndex = ZOOM_STEPS.indexOf(1);
        this.updateControls();
        await this.renderCurrentPage();
    }

    handlePageInput(event) {
        if (event.key !== "Enter") {
            return;
        }
        event.preventDefault();
        const requestedPage = Number.parseInt(this.pageInput.value, 10);
        if (Number.isNaN(requestedPage)) {
            this.syncPageInput();
            return;
        }
        this.goToPage(requestedPage);
    }

    handleKeyboard(event) {
        if (isTypingTarget(document.activeElement)) {
            return;
        }
        if (event.key === "ArrowLeft" || event.key === "PageUp") {
            event.preventDefault();
            this.goToPage(this.currentPage - 1);
        }
        if (event.key === "ArrowRight" || event.key === "PageDown") {
            event.preventDefault();
            this.goToPage(this.currentPage + 1);
        }
    }

    handleResize() {
        if (!this.pdfDocument) {
            return;
        }
        window.clearTimeout(this.resizeTimer);
        this.resizeTimer = window.setTimeout(() => {
            this.renderCurrentPage();
        }, RESIZE_DEBOUNCE_MS);
    }

    async toggleFullscreen() {
        if (!document.fullscreenEnabled) {
            return;
        }
        if (document.fullscreenElement === this.root) {
            await document.exitFullscreen();
        } else {
            await this.root.requestFullscreen();
        }
    }

    async renderCurrentPage() {
        if (!this.pdfDocument || !this.frame.clientWidth || !this.frame.clientHeight) {
            return;
        }

        const token = ++this.renderToken;
        if (this.renderTask) {
            this.renderTask.cancel();
            this.renderTask = null;
        }

        this.root.classList.add("is-loading");
        this.root.classList.remove("has-error");
        this.error.hidden = true;

        try {
            const page = await this.pdfDocument.getPage(this.currentPage);
            if (token !== this.renderToken) {
                return;
            }

            const baseViewport = page.getViewport({ scale: 1 });
            const fitScale = this.fitScaleFor(baseViewport);
            const scale = fitScale * ZOOM_STEPS[this.zoomIndex];
            const viewport = page.getViewport({ scale });
            const ratio = window.devicePixelRatio || 1;
            const context = this.canvas.getContext("2d");

            this.canvas.width = Math.floor(viewport.width * ratio);
            this.canvas.height = Math.floor(viewport.height * ratio);
            this.canvas.style.width = `${Math.floor(viewport.width)}px`;
            this.canvas.style.height = `${Math.floor(viewport.height)}px`;

            context.setTransform(ratio, 0, 0, ratio, 0, 0);
            context.clearRect(0, 0, viewport.width, viewport.height);

            this.renderTask = page.render({ canvasContext: context, viewport });
            await this.renderTask.promise;

            if (token !== this.renderToken) {
                return;
            }

            this.renderTask = null;
            this.root.classList.remove("is-loading");
            this.centerCurrentPage();
        } catch (error) {
            if (error?.name === "RenderingCancelledException") {
                return;
            }
            this.showError();
            console.error("PDF lesson viewer failed to render", error);
        }
    }

    fitScaleFor(viewport) {
        const styles = window.getComputedStyle(this.frame);
        const horizontalPadding = Number.parseFloat(styles.paddingLeft) + Number.parseFloat(styles.paddingRight);
        const verticalPadding = Number.parseFloat(styles.paddingTop) + Number.parseFloat(styles.paddingBottom);
        const availableWidth = Math.max(1, this.frame.clientWidth - horizontalPadding);
        const availableHeight = Math.max(1, this.frame.clientHeight - verticalPadding);
        return Math.min(availableWidth / viewport.width, availableHeight / viewport.height);
    }

    centerCurrentPage() {
        this.frame.scrollLeft = Math.max(0, (this.frame.scrollWidth - this.frame.clientWidth) / 2);
        this.frame.scrollTop = Math.max(0, (this.frame.scrollHeight - this.frame.clientHeight) / 2);
    }

    syncPageInput() {
        this.pageInput.value = String(this.currentPage);
    }

    updateControls() {
        this.syncPageInput();
        this.prevButton.disabled = this.currentPage <= 1;
        this.nextButton.disabled = this.totalPages === 0 || this.currentPage >= this.totalPages;
        this.zoomOutButton.disabled = this.zoomIndex <= 0;
        this.zoomInButton.disabled = this.zoomIndex >= ZOOM_STEPS.length - 1;
        this.fitButton.textContent = this.zoomIndex === ZOOM_STEPS.indexOf(1)
            ? "Ajustar"
            : `${Math.round(ZOOM_STEPS[this.zoomIndex] * 100)}%`;
    }

    showError() {
        this.root.classList.remove("is-loading");
        this.root.classList.add("has-error");
        this.error.hidden = false;
    }
}

document.querySelectorAll(".js-pdf-viewer").forEach((viewer) => {
    new LessonPdfViewer(viewer).init();
});
