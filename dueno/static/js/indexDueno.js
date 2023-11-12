// Añade este script a tu archivo JS

function mostrarPopup(id) {
    var popup = document.getElementById(id);
    popup.style.display = "flex";
}

function cerrarPopup(id) {
    var popup = document.getElementById(id);
    popup.style.display = "none";
}

function mostrarCargando() {
    window.location.href = "{% url 'cargando/' %}";

    // Simula una carga durante 2 segundos antes de redirigir a la página de cliente
    setTimeout(function() {
        window.location.href = "{% url 'cargando/' %}";
    }, 2000);
}