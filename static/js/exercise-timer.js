(function () {
    const root = document.querySelector('[data-timer-root]');
    if (!root) return;

    const display = root.querySelector('[data-timer-display]');
    const toggle = root.querySelector('[data-timer-toggle]');
    const disable = root.querySelector('[data-timer-disable]');
    const live = root.querySelector('[data-timer-live]');
    const form = document.querySelector('[data-exercise-timer-form]');
    const durationInput = document.querySelector('[data-timer-duration-input]');
    const enabledInput = document.querySelector('[data-timer-enabled-input]');
    const pausedInput = document.querySelector('[data-timer-paused-input]');
    const syncUrl = root.dataset.syncUrl;

    let duration = parseInt(root.dataset.duration || '0', 10);
    let enabled = root.dataset.enabled === '1';
    let manuallyPaused = root.dataset.paused === '1';
    let visiblePaused = document.hidden;
    let lastTick = Date.now();
    let syncTimer = null;

    function writeState() {
        durationInput.value = String(Math.max(0, Math.floor(duration)));
        enabledInput.value = enabled ? '1' : '0';
        pausedInput.value = manuallyPaused ? '1' : '0';
    }

    function render() {
        const total = Math.max(0, Math.floor(duration));
        const minutes = Math.floor(total / 60);
        const seconds = total % 60;
        display.textContent = String(minutes).padStart(2, '0') + ':' + String(seconds).padStart(2, '0');
        toggle.textContent = manuallyPaused ? 'Reanudar' : 'Pausar';
        toggle.setAttribute('aria-label', manuallyPaused ? 'Reanudar cronometro' : 'Pausar cronometro');
        disable.textContent = enabled ? 'Desactivar' : 'Activar';
        disable.setAttribute('aria-label', enabled ? 'Desactivar cronometro' : 'Activar cronometro');
        root.classList.toggle('exercise-timer-paused', !enabled || manuallyPaused || visiblePaused);
        writeState();
    }

    function tick() {
        const now = Date.now();
        if (enabled && !manuallyPaused && !visiblePaused) {
            duration += (now - lastTick) / 1000;
        }
        lastTick = now;
        render();
    }

    function sync(useBeacon) {
        tick();
        const payload = JSON.stringify({
            duration_seconds: Math.max(0, Math.floor(duration)),
            timer_enabled: enabled,
            timer_paused: manuallyPaused
        });
        if (useBeacon && navigator.sendBeacon) {
            const blob = new Blob([payload], { type: 'application/json' });
            navigator.sendBeacon(syncUrl, blob);
            return Promise.resolve();
        }
        return fetch(syncUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: payload,
            credentials: 'same-origin'
        }).catch(function () {
            live.textContent = 'No se pudo sincronizar el cronometro. Tus respuestas se pueden guardar igualmente.';
        });
    }

    toggle.addEventListener('click', function () {
        tick();
        manuallyPaused = !manuallyPaused;
        live.textContent = manuallyPaused ? 'Cronometro pausado.' : 'Cronometro reanudado.';
        render();
        sync(false);
    });

    disable.addEventListener('click', function () {
        tick();
        enabled = !enabled;
        if (enabled) manuallyPaused = false;
        live.textContent = enabled ? 'Cronometro activado.' : 'Cronometro desactivado.';
        render();
        sync(false);
    });

    document.addEventListener('visibilitychange', function () {
        tick();
        visiblePaused = document.hidden;
        render();
        sync(false);
    });

    window.addEventListener('beforeunload', function () {
        sync(true);
    });

    if (form) {
        form.addEventListener('submit', function () {
            tick();
            writeState();
        });
    }

    render();
    setInterval(tick, 1000);
    syncTimer = setInterval(function () { sync(false); }, 20000);
})();
