const puntosDeInteres = {
    // Itera sobre los puntos de interés y crea objetos JavaScript
    {% for punto in punto_intereses %}
        {
            id: {{ punto.id }},
            latitud: {{ punto.latitud }},
            longitud: {{ punto.longitud }},
            nombre: "{{ punto.nombre }}"
        },
    {% endfor %}
    }