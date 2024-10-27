document.addEventListener('DOMContentLoaded', function() {
    var deleteLinks = document.querySelectorAll('.btn-delete');

    deleteLinks.forEach(function(link) {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            var targetUrl = this.getAttribute('href');
            
            var modal = new bootstrap.Modal(document.getElementById('confirmModal'));
            var confirmDeleteButton = document.getElementById('confirmDelete');
            
            confirmDeleteButton.setAttribute('href', targetUrl);
            modal.show();
        });
    });
});
