
document.addEventListener('DOMContentLoaded', function() {
    const toggleBtn = document.getElementById('toggleSidebar');
    const sidebar = document.querySelector('.sidebar');
    const content = document.querySelector('.content');
    
    
    document.body.classList.add('no-transition');
    
    
    const menuState = localStorage.getItem('menuState');
    if (menuState === 'collapsed') {
        sidebar.classList.add('sidebar-collapsed');
        content.classList.add('content-expanded');
    }
    
    toggleBtn.addEventListener('click', function() {
        sidebar.classList.toggle('sidebar-collapsed');
        content.classList.toggle('content-expanded');
    
        if (sidebar.classList.contains('sidebar-collapsed')) {
            localStorage.setItem('menuState', 'collapsed');
        } else {
            localStorage.setItem('menuState', 'expanded');
        }
    });
    
    
    setTimeout(function() {
        document.body.classList.remove('no-transition');
    }, 50);
    });
    
    
    
    function setFontSize(size) {
    document.documentElement.classList.remove('font-small', 'font-medium', 'font-large');
    document.documentElement.classList.add('font-' + size);
    localStorage.setItem('fontSize', size);
    }
    
    
    
    document.addEventListener('DOMContentLoaded', function() {
        
    
        function toggleDarkMode() {
            document.body.classList.toggle('dark-mode');
            const isDarkMode = document.body.classList.contains('dark-mode');
            localStorage.setItem('dark-mode', isDarkMode);
        }
    
        if (localStorage.getItem('dark-mode') === 'true') {
            document.body.classList.add('dark-mode');
        }
    
        function resetAccessibility() {
            document.body.style.fontSize = '';
            document.body.classList.remove('dark-mode');
        }
        
        window.toggleDarkMode = toggleDarkMode;
    });