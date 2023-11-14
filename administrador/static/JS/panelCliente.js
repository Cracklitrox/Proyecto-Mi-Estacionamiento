// Obtener el elemento que tiene la imagen de la flecha
var flecha = document.getElementById("flecha");

// Obtener el elemento que tiene el contenido del drop down
var contenido = document.getElementById("contenido");

// Crear una función que se ejecute cuando el usuario haga clic en la imagen
function toggleDropdown() {
    // Si el contenido está oculto, mostrarlo
    if (contenido.style.display == "none") {
        contenido.style.display = "block";
    }
    // Si el contenido está visible, ocultarlo
    else {
        contenido.style.display = "none";
    }
}

// Añadir un evento de clic a la imagen que llame a la función
flecha.addEventListener("click", toggleDropdown);

$(document).ready(function () {
    $("#alertaMensaje").delay(3000).fadeOut("slow");
});