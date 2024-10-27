function togglePassword(inputId) {
    const input = document.getElementById(inputId);
    const button = input.nextElementSibling;
    if (input.type === 'password') {
        input.type = 'text';
        button.textContent = '👁️';
    } else {
        input.type = 'password';
        button.textContent = '👁️';
    }
}

document.getElementById('registerForm').addEventListener('submit', function (e) {
    e.preventDefault();
    if (validateForm()) {
        console.log('Formulario enviado');
        showNotification('Registro exitoso! Bienvenido a Bonanza.');
        setTimeout(() => {
            const loginUrl = e.target.getAttribute('data-login-url'); 
            window.location.assign(loginUrl); 
        }, 1000);
        // Aquí iría la lógica para enviar los datos al servidor
    }
});

function validateForm() {
    let isValid = true;
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;

  
    if (username.trim() === '') {
        showError('usernameError', 'El nombre de usuario es requerido');
        isValid = false;
    } else if (username.length < 3) {
        showError('usernameError', 'El nombre de usuario debe tener al menos 3 caracteres');
        isValid = false;
    } else {
        showError('usernameError', '');
    }

    
    if (email.trim() === '') {
        showError('emailError', 'El correo electrónico es requerido');
        isValid = false;
    } else if (!/\S+@\S+\.\S+/.test(email)) {
        showError('emailError', 'Correo electrónico inválido');
        isValid = false;
    } else {
        showError('emailError', '');
    }

    
    if (password.trim() === '') {
        showError('passwordError', 'La contraseña es requerida');
        isValid = false;
    } else if (password.length < 6) {
        showError('passwordError', 'La contraseña debe tener al menos 6 caracteres');
        isValid = false;
    } else if (!/(?=.*[a-z])(?=.*[A-Z])(?=.*\d)/.test(password)) {
        showError('passwordError', 'La contraseña debe contener al menos una letra minúscula, una mayúscula y un número');
        isValid = false;
    } else {
        showError('passwordError', '');
    }

    
    if (password !== confirmPassword) {
        showError('confirmPasswordError', 'Las contraseñas no coinciden');
        isValid = false;
    } else {
        showError('confirmPasswordError', '');
    }

    return isValid;
}

function showError(id, message) {
    const errorElement = document.getElementById(id);
    errorElement.textContent = message;
    errorElement.style.display = message ? 'block' : 'none';
}

function showNotification(message) {
    const notificationBar = document.getElementById('notificationBar');
    notificationBar.textContent = message;
    notificationBar.classList.add('active');
    setTimeout(() => {
        notificationBar.classList.remove('active');
    }, 1000); 
}
