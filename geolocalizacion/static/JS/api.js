let map;

async function initMap() {
    map = new google.maps.Map(document.getElementById("mapDiv"), {
        center: { lat: -34.397, lng: 150.644 },
        zoom: 8,
    });

    // Resto del código...
}

// Llama a initMap después de cargar la API de Google Maps


// const mapDiv = document.getElementById("map");
//     const input = document.getElementById("place_input");
//     let map;    
//     let marker;
//     let autoComplete;

    // const shopCoord = { 
    //   lat: -41.477492,
    //   lng: -72.990633,
    //   name: 'Tinta en Acción'
    // };

    // function initMap() {
    //   map = new google.maps.Map(mapDiv, {
    //     center: shopCoord,
    //     zoom: 15
    //   });


    //   const markerIcon = {
    //     url: '../IMG/geo-alt-fill.svg', // Ruta al archivo SVG descargado
    //     scaledSize: new google.maps.Size(40, 40), // Tamaño del ícono
    //     origin: new google.maps.Point(0, 0), // Origen del ícono
    //     anchor: new google.maps.Point(20, 40) // Punto de anclaje del ícono
    //   };

    //   marker = new google.maps.Marker ({
    //     position: shopCoord,
    //     map: map,
    //     draggable: true,
    //     icon: markerIcon,
    //     title: 'Marcador Personalizado'
    //   });

    //   initAutoComplete();
    // }

    // function initAutoComplete(){
    //   autoComplete = new google.maps.places.Autocomplete(input); 

    //   input.addEventListener('focus', function () {
    //     input.value = shopCoord.name;
    //     map.setCenter(shopCoord);
    //     map.setZoom(15);
    //     marker.setPosition(shopCoord);
    //   });

    //   autoComplete.addListener('place_changed', function () {
    //     const place = autoComplete.getPlace();
    //     console.log(place);
    //     map.setCenter(place.geometry.location);
    //     map.setZoom(12);
    //     marker.setPosition(place.geometry.location);
    //   });
    // }