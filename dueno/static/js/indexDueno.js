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

function cambiarEstado() {
    $(document).ready(function () {
        $('.btn-cambiar-estado').click(function () {
            var estacionamientoId = $(this).data('estacionamiento-id');

            $.ajax({
                type: 'POST',
                url: '/indexDueno/cambiar_estado/' + estacionamientoId + '/',  // Elimina el prefijo '/dueno/indexDueno/'
                success: function (data) {
                    // Maneja la respuesta del servidor, por ejemplo, actualizando la interfaz de usuario
                    if (data.estado) {
                        alert('Estacionamiento habilitado.');
                    } else {
                        alert('Estacionamiento deshabilitado.');
                    }
                },
                error: function (error) {
                    console.log('Error al cambiar el estado del estacionamiento:', error);
                }
            });
        });
    });
}


