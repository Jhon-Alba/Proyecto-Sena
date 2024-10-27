document.addEventListener("DOMContentLoaded", function() {
    const celularInput = document.querySelector('input[name="numero_celular"]');
    const emailInput = document.querySelector('input[name="correo_electronico"]');

    document.querySelector('input[name="nombre"]').addEventListener('input', function(e) {
        const value = e.target.value;
        if (/^(?:[a-zA-ZáéíóúÁÉÍÓÚñÑ]+(?:\s+[a-zA-ZáéíóúÁÉÍÓÚñÑ]+)*)?$/.test(value) === false) {
            e.target.setCustomValidity('El nombre solo debe contener letras y no debe incluir números ni caracteres especiales.');
        } else {
            e.target.setCustomValidity('');
        }
    });

    celularInput.addEventListener('input', function(e) {
        const value = e.target.value;
        if (/^\d+$/.test(value) === false) {
            e.target.setCustomValidity('El número de celular debe contener solo dígitos y ser positivo.');
        } else if (parseInt(value) < 0) {
            e.target.setCustomValidity('El número de celular no puede ser negativo.');
        } else if (value.length > 10) {
            e.target.setCustomValidity('El número de celular no debe exceder los 10 dígitos.');
        } else {
            e.target.setCustomValidity('');
        }
    });

    emailInput.addEventListener('input', function(e) {
        const value = e.target.value;
        if (!/@/.test(value)) {
            e.target.setCustomValidity('El correo electrónico debe contener el símbolo "@".');
        } else {
            e.target.setCustomValidity('');
        }
    });
});