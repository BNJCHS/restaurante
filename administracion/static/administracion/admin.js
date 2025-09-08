document.addEventListener('DOMContentLoaded', () => {
    const links = document.querySelectorAll('.sidebar a[data-section]');
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
            .then(html => {
                content.innerHTML = html;
            })
            .catch(err => {
                content.innerHTML = `<p style="color:red;">Error cargando sección: ${err}</p>`;
            });
    }

    // Cargar dashboard por defecto
    loadSection('dashboard');
});

// Funciones AJAX de edición
function loadEditPedido(id) {
    fetch(`/administracion/pedidos/${id}/editar/`)
        .then(r => r.text())
        .then(html => {
            document.getElementById("admin-content").innerHTML = html;
        });
}

function loadEditReserva(id) {
    fetch(`/administracion/reservas/${id}/editar/`)
        .then(r => r.text())
        .then(html => {
            document.getElementById("admin-content").innerHTML = html;
        });
}
