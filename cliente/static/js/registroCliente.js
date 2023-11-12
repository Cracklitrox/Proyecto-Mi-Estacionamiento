document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('registrationForm');
    const runInput = document.getElementById('run');
    const dvRunInput = document.getElementById('dv_run');
    const emailInput = document.getElementById('correoElectronico');
    const telefonoInput = document.getElementById('telefono');

    form.addEventListener('submit', function (event) {
        let valid = true;

        // Validar RUN y DV RUN (solo números)
        if (!/^\d+$/.test(runInput.value) || !/^\d+$/.test(dvRunInput.value)) {
            valid = false;
            showError(runInput, 'Ingresa solo números en RUN y DV RUN');
        } else {
            clearError(runInput);
        }

        // Validar correo electrónico
        if (!isValidEmail(emailInput.value)) {
            valid = false;
            showError(emailInput, 'Ingresa un correo electrónico válido');
        } else {
            clearError(emailInput);
        }

        // Validar teléfono (solo números)
        if (!/^\d+$/.test(telefonoInput.value)) {
            valid = false;
            showError(telefonoInput, 'Ingresa solo números en el teléfono');
        } else {
            clearError(telefonoInput);
        }

        if (!valid) {
            event.preventDefault();
        }
    });

    function showError(input, message) {
        const errorDiv = document.createElement('div');
        errorDiv.className = 'error';
        errorDiv.textContent = message;

        input.parentNode.insertBefore(errorDiv, input.nextSibling);
    }

    function clearError(input) {
        const errorDiv = input.nextSibling;
        if (errorDiv && errorDiv.className === 'error') {
            input.parentNode.removeChild(errorDiv);
        }
    }

    function isValidEmail(email) {
        // Patrón simple para verificar el formato de correo electrónico
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailPattern.test(email);
    }
});
