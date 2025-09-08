document.addEventListener('DOMContentLoaded', () => {
    const links = document.querySelectorAll('nav ul li a[data-section]');
    const content = document.getElementById('admin-content');

    links.forEach(link => {
        link.addEventListener('click', e => {
            e.preventDefault();
            const section = link.getAttribute('data-section');
            loadSection(section);
        });
    });

    function loadSection(section) {
        fetch(`/administracion/ajax/${section}/`)
            .then(response => response.text())
            .then(html => content.innerHTML = html)
            .catch(err => content.innerHTML = `<p style="color:red;">Error cargando sección: ${err}</p>`);
    }

    // Cargar dashboard por defecto
    loadSection('dashboard');
});
