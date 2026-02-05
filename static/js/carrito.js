
let pedido = JSON.parse(localStorage.getItem('pedido')) || [];




// Función para el numerito rojo del menú
function actualizarContador() {
    const contador = document.getElementById('carrito-count');
    if (!contador) return;

    let carrito = JSON.parse(localStorage.getItem('carrito')) || [];
    let cantidadTotal = carrito.reduce((total, item) => total + item.cantidad, 0);

    if (cantidadTotal > 0) {
        contador.innerText = cantidadTotal;
        contador.style.display = 'inline-block';
    } else {
        contador.style.display = 'none';
    }
}

// Cargar contador al iniciar la página
document.addEventListener('DOMContentLoaded', actualizarContador);