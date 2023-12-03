$(document).ready(function () {
    $('.slick-carousel').slick({
        slidesToShow: 3,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 5000,
        prevArrow: $('.slick-prev'),
        nextArrow: $('.slick-next'),
    });
});
const imageUrl = "{% static 'img/geo-alt-fill.svg' %}";
const mapDiv = document.getElementById("map");
let map;
let marker;
let marcadorArray = []; // Array para almacenar marcadores

const puntosDeInteres = [
    {% for punto in puntos_interes %}
{
    id: { { punto.id } },
    latitud: { { punto.latitud } },
    longitud: { { punto.longitud } },
    nombre: "{{ punto.nombre }}"
},
{% endfor %}
          // Agrega más puntos de interés según tus necesidades
    ];

const santiagoCoords = {
    lat: -33.45694,
    lng: -70.64827,
    name: 'Santiago'
};



function initMap() {
    map = new google.maps.Map(mapDiv, {
        center: santiagoCoords,
        zoom: 15
    });

    // Manejar cambios en el select
    document.getElementById('PuntoSelect').addEventListener('change', manejarPuntoSelect);

    // Mostrar el primer punto de interés al cargar la página
    manejarPuntoSelect();
}

function manejarPuntoSelect() {
    const selectPuntoId = document.getElementById('PuntoSelect').value;
    const selectPuntoI = puntosDeInteres.find(poi => poi.id == selectPuntoId);

    // Verificar si selectPuntoI está definido antes de acceder a sus propiedades
    if (selectPuntoI) {
        // Limpiar todos los marcadores antes de agregar uno nuevo
        limpiarMarcadores();

        // Mostrar el nuevo marcador
        marker = new google.maps.Marker({
            position: { lat: parseFloat(selectPuntoI.latitud), lng: parseFloat(selectPuntoI.longitud) },
            map: map,
            icon: {
                url: imageUrl,
                scaledSize: new google.maps.Size(40, 40),
                origin: new google.maps.Point(0, 0),
                anchor: new google.maps.Point(20, 40)
            },
            title: selectPuntoI.nombre
        });

        // Agregar el nuevo marcador al array
        marcadorArray.push(marker);

        // Centrar el mapa en el nuevo marcador
        map.setCenter(marker.getPosition());
    } else {
        console.error(`No se encontró ningún punto de interés con id ${selectPuntoId}`);
    }
}

function limpiarMarcadores() {
    // Iterar sobre el array y configurar el mapa como nulo para cada marcador
    for (let i = 0; i < marcadorArray.length; i++) {
        marcadorArray[i].setMap(null);
    }
    // Limpiar el array
    marcadorArray = [];
}