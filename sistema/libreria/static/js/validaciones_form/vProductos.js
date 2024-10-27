document.addEventListener("DOMContentLoaded", function() {

    document.querySelector('input[name="nombre"]').addEventListener('input', function(e) {
        const value = e.target.value;
        if (/^(?:[a-zA-ZáéíóúÁÉÍÓÚñÑ]+(?:\s+[a-zA-ZáéíóúÁÉÍÓÚñÑ]+)*)?$/.test(value) === false) {
            e.target.setCustomValidity('El nombre solo debe contener letras y no debe incluir números ni caracteres especiales.');
        } else {
            e.target.setCustomValidity('');
        }
    });

    document.querySelector('input[name="precio"]').addEventListener('input', function(e) {
        const value = e.target.value;
        if (/[^0-9.]/.test(value)) {
            e.target.setCustomValidity('El precio debe estar en positivo y no debe contener letras.');
        } else {
            e.target.setCustomValidity('');
        }
    });
});