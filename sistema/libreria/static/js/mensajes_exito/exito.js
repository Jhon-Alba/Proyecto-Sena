document.addEventListener('DOMContentLoaded', function () {
    var message = document.getElementById('message');
    if (message) {
        setTimeout(function () {
            message.classList.add('fade');
            setTimeout(function () {
                message.style.display = 'none';
            }, 500);
        }, 3000); 
    }
});
