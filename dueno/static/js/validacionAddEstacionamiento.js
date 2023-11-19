function validarFormulario() {
    // Realiza tu lógica de validación aquí
    var direccion = document.getElementById('id_direccion').value;
    var tarifaHora = document.getElementById('id_tarifahora').value;

    if (tarifaHora < 0){
        alert('La tarifa por hora debe ser mayor o igual a cero.')
        return false;
    }

    // Puedes agregar más validaciones según tus necesidades

    return true;  // Devuelve true si el formulario es válido
}