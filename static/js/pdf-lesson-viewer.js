const ZOOM_LEVELS = [0.8, 0.9, 1, 1.1, 1.25, 1.5, 1.75, 2];
const RESIZE_DELAY = 140;

class LessonPdfViewer {
    constructor(root) {
        this.root = root;
        this.workspace = root.querySelector('[data-workspace]');
        this.canvas = root.querySelector('[data-pdf-canvas]');
        this.context = this.canvas.getContext('2d');
        this.loadingMessage = root.querySelector('[data-loading-message]');
        this.errorMessage = root.querySelector('[data-error-message]');
        this.statusLabel = root.querySelector('[data-pdf-status]');
        this.pageTotalBadge = document.querySelector('[data-pdf-page-total]');
        this.pageAnnouncer = root.querySelector('[data-page-announcer]');
        this.pageInput = root.querySelector('[data-page-input]');
        this.totalPagesLabel = root.querySelector('[data-total-pages]');
        this.zoomLabel = root.querySelector('[data-zoom-label]');
        this.buttons = {
            previous: root.querySelector('[data-action="previous"]'),
            next: root.querySelector('[data-action="next"]'),
            zoomOut: root.querySelector('[data-action="zoom-out"]'),
            zoomIn: root.querySelector('[data-action="zoom-in"]'),
            fit: root.querySelector('[data-action="fit"]'),
            fullscreen: root.querySelector('[data-action="fullscreen"]'),
        };

        this.pdfDocument = null;
        this.currentPage = 1;
        this.totalPages = 0;
        this.fitScale = 1;
        this.userZoomFactor = 1;
        this.renderTask = null;
        this.renderSequence = 0;
        this.resizeTimer = null;
        this.documentTitle = root.dataset.documentTitle || 'PDF';
    }

    async init() {
        this.bindEvents();
        this.setControlsEnabled(false);

        try {
            const pdfjsLib = await import(this.root.dataset.pdfjsUrl);
            pdfjsLib.GlobalWorkerOptions.workerSrc = this.root.dataset.workerUrl;
            this.pdfDocument = await pdfjsLib.getDocument({ url: this.root.dataset.pdfUrl }).promise;
            this.totalPages = this.pdfDocument.numPages;
            this.totalPagesLabel.textContent = String(this.totalPages);
            this.pageInput.max = String(this.totalPages);
            this.updatePageCountBadge();
            this.setControlsEnabled(true);
            await this.renderCurrentPage({ announce: false });
        } catch (error) {
            this.showError();
        }
    }

    bindEvents() {
        this.buttons.previous.addEventListener('click', () => this.goToPage(this.currentPage - 1));
        this.buttons.next.addEventListener('click', () => this.goToPage(this.currentPage + 1));
        this.buttons.zoomOut.addEventListener('click', () => this.changeZoom(-1));
        this.buttons.zoomIn.addEventListener('click', () => this.changeZoom(1));
        this.buttons.fit.addEventListener('click', () => this.fitPage());
        this.pageInput.addEventListener('keydown', (event) => this.handlePageInput(event));

        if (document.fullscreenEnabled) {
            this.buttons.fullscreen.addEventListener('click', () => this.toggleFullscreen());
            document.addEventListener('fullscreenchange', () => this.handleFullscreenChange());
        } else {
            this.buttons.fullscreen.hidden = true;
        }

        document.addEventListener('keydown', (event) => this.handleKeyboard(event));

        this.resizeObserver = new ResizeObserver(() => this.debouncedResize());
        this.resizeObserver.observe(this.workspace);
    }

    setControlsEnabled(enabled) {
        [
            this.buttons.previous,
            this.buttons.next,
            this.buttons.zoomOut,
            this.buttons.zoomIn,
            this.buttons.fit,
            this.pageInput,
        ].forEach((control) => {
            control.disabled = !enabled;
        });
        this.updateControls();
    }

    updateControls() {
        const ready = Boolean(this.pdfDocument);
        this.buttons.previous.disabled = !ready || this.currentPage <= 1;
        this.buttons.next.disabled = !ready || this.currentPage >= this.totalPages;
        this.buttons.zoomOut.disabled = !ready || this.userZoomFactor <= ZOOM_LEVELS[0];
        this.buttons.zoomIn.disabled = !ready || this.userZoomFactor >= ZOOM_LEVELS[ZOOM_LEVELS.length - 1];
        this.buttons.fit.disabled = !ready || this.userZoomFactor === 1;
        this.pageInput.disabled = !ready;
        this.pageInput.value = String(this.currentPage);
        this.zoomLabel.textContent = this.userZoomFactor === 1
            ? 'Ajustar'
            : `${Math.round(this.userZoomFactor * 100)}%`;
    }

    updatePageCountBadge() {
        if (!this.pageTotalBadge) {
            return;
        }
        this.pageTotalBadge.textContent = `${this.totalPages} páginas`;
        this.pageTotalBadge.hidden = false;
    }

    async goToPage(pageNumber) {
        if (!this.pdfDocument) {
            return;
        }
        const nextPage = Number(pageNumber);
        if (!Number.isInteger(nextPage) || nextPage < 1 || nextPage > this.totalPages || nextPage === this.currentPage) {
            this.pageInput.value = String(this.currentPage);
            return;
        }
        this.currentPage = nextPage;
        await this.renderCurrentPage({ announce: true });
    }

    async renderCurrentPage({ announce }) {
        const sequence = ++this.renderSequence;

        if (this.renderTask) {
            this.renderTask.cancel();
            this.renderTask = null;
        }

        this.setRenderingState(true);

        try {
            const page = await this.pdfDocument.getPage(this.currentPage);
            if (sequence !== this.renderSequence) {
                return;
            }

            const baseViewport = page.getViewport({ scale: 1 });
            this.fitScale = this.calculateFitScale(baseViewport);
            const renderScale = this.fitScale * this.userZoomFactor;
            const deviceRatio = window.devicePixelRatio || 1;
            const viewport = page.getViewport({ scale: renderScale });

            this.canvas.width = Math.floor(viewport.width * deviceRatio);
            this.canvas.height = Math.floor(viewport.height * deviceRatio);
            this.canvas.style.width = `${viewport.width}px`;
            this.canvas.style.height = `${viewport.height}px`;
            this.context.setTransform(deviceRatio, 0, 0, deviceRatio, 0, 0);
            this.context.clearRect(0, 0, viewport.width, viewport.height);

            this.renderTask = page.render({
                canvasContext: this.context,
                viewport,
            });
            await this.renderTask.promise;
            if (sequence !== this.renderSequence) {
                return;
            }

            this.canvas.hidden = false;
            this.canvas.setAttribute('aria-label', `Página ${this.currentPage} de ${this.totalPages} del documento ${this.documentTitle}`);
            this.statusLabel.textContent = `Página ${this.currentPage} de ${this.totalPages}`;
            if (announce) {
                this.pageAnnouncer.textContent = `Página ${this.currentPage} de ${this.totalPages}`;
            }
        } catch (error) {
            if (error?.name !== 'RenderingCancelledException') {
                this.showError();
            }
        } finally {
            if (sequence === this.renderSequence) {
                this.renderTask = null;
                this.setRenderingState(false);
                this.updateControls();
            }
        }
    }

    calculateFitScale(viewport) {
        const styles = window.getComputedStyle(this.workspace);
        const paddingX = parseFloat(styles.paddingLeft) + parseFloat(styles.paddingRight);
        const paddingY = parseFloat(styles.paddingTop) + parseFloat(styles.paddingBottom);
        const availableWidth = Math.max(120, this.workspace.clientWidth - paddingX);
        const availableHeight = Math.max(160, this.workspace.clientHeight - paddingY);
        return Math.min(availableWidth / viewport.width, availableHeight / viewport.height);
    }

    setRenderingState(isRendering) {
        this.loadingMessage.hidden = !isRendering;
        this.statusLabel.textContent = isRendering ? 'Renderizando página' : this.statusLabel.textContent;
    }

    showError() {
        this.loadingMessage.hidden = true;
        this.canvas.hidden = true;
        this.errorMessage.hidden = false;
        this.statusLabel.textContent = 'Error del visor';
        this.setControlsEnabled(false);
    }

    async changeZoom(direction) {
        const currentIndex = ZOOM_LEVELS.indexOf(this.userZoomFactor);
        const fallbackIndex = ZOOM_LEVELS.findIndex((level) => level >= this.userZoomFactor);
        const startIndex = currentIndex >= 0 ? currentIndex : Math.max(0, fallbackIndex);
        const nextIndex = Math.min(ZOOM_LEVELS.length - 1, Math.max(0, startIndex + direction));
        this.userZoomFactor = ZOOM_LEVELS[nextIndex];
        await this.renderCurrentPage({ announce: false });
    }

    async fitPage() {
        this.userZoomFactor = 1;
        await this.renderCurrentPage({ announce: false });
    }

    handlePageInput(event) {
        if (event.key !== 'Enter') {
            return;
        }
        event.preventDefault();
        this.goToPage(Number(this.pageInput.value));
    }

    handleKeyboard(event) {
        if (!this.pdfDocument || this.isEditableElement(event.target)) {
            return;
        }
        if (event.key === 'ArrowLeft') {
            event.preventDefault();
            this.goToPage(this.currentPage - 1);
        }
        if (event.key === 'ArrowRight') {
            event.preventDefault();
            this.goToPage(this.currentPage + 1);
        }
    }

    isEditableElement(element) {
        const tagName = element?.tagName?.toLowerCase();
        return ['input', 'textarea', 'select'].includes(tagName) || element?.isContentEditable;
    }

    debouncedResize() {
        window.clearTimeout(this.resizeTimer);
        this.resizeTimer = window.setTimeout(() => {
            if (this.pdfDocument) {
                this.renderCurrentPage({ announce: false });
            }
        }, RESIZE_DELAY);
    }

    async toggleFullscreen() {
        if (!document.fullscreenElement) {
            await this.root.requestFullscreen();
        } else {
            await document.exitFullscreen();
        }
    }

    handleFullscreenChange() {
        const isFullscreen = document.fullscreenElement === this.root;
        this.root.classList.toggle('is-fullscreen', isFullscreen);
        this.buttons.fullscreen.setAttribute(
            'aria-label',
            isFullscreen ? 'Salir de pantalla completa' : 'Ver en pantalla completa'
        );
        this.buttons.fullscreen.innerHTML = isFullscreen
            ? '<i class="fas fa-compress" aria-hidden="true"></i>'
            : '<i class="fas fa-expand" aria-hidden="true"></i>';
        this.debouncedResize();
    }
}

document.querySelectorAll('[data-pdf-viewer]').forEach((viewer) => {
    new LessonPdfViewer(viewer).init();
});
