const pedidoBtn = document.getElementById('pedido-btn');
const reservaBtn = document.getElementById('reserva-btn');
const pedidoForm = document.getElementById('pedido-form');
const reservaForm = document.getElementById('reserva-form');
const formContainer = document.getElementById('form-container');

pedidoBtn.addEventListener('click', () => {
    formContainer.classList.remove('hidden');
    pedidoForm.classList.remove('hidden');
    reservaForm.classList.add('hidden');
});

reservaBtn.addEventListener('click', () => {
    formContainer.classList.remove('hidden');
    reservaForm.classList.remove('hidden');
    pedidoForm.classList.add('hidden');
});
