document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('quizForm');
    const submitBtn = document.getElementById('submitBtn');
    const progressBar = document.getElementById('progressBar');
    const questionCount = Number(form.dataset.questionCount);
    const radioButtons = document.querySelectorAll('input[type="radio"]');

    function updateProgress() {
        const answeredCount = form.querySelectorAll('input[type="radio"]:checked').length;
        const progressPercent = (answeredCount / questionCount) * 100;

        progressBar.style.width = progressPercent + '%';
        progressBar.setAttribute('aria-valuenow', progressPercent);
        progressBar.textContent = Math.round(progressPercent) + '%';
        submitBtn.disabled = answeredCount < questionCount;
    }

    radioButtons.forEach(function(radio) {
        radio.addEventListener('change', updateProgress);
    });

    updateProgress();
});
