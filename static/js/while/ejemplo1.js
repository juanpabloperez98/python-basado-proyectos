(function () {
    // Variables globales
    var num_inputs = 1,
        i = 0,
        lista_datos = []

    // Salida
    salida = () => {
        var nota,
            suma = 0,
            numero_veces = lista_datos.length;
        for (let i = 0; i < lista_datos.length; i++) {
            nota = lista_datos[i]
            suma += nota
        }
        promedio = suma/numero_veces
        document.getElementById('salida').innerHTML = "Promedio es: " + promedio.toString()
    }

    explicacion = () => { /* La función */
        document.getElementById('explicacion').setAttribute('class', 'col-lg-5 mt-3 mx-auto bg-light')
        document.getElementById('explicar').removeEventListener('click', explicacion)
        document.getElementById('explicar').setAttribute('class', 'desactivate')
        document.getElementById('reiniciar').setAttribute('class', 'btn botonBlue')
    }

    // Comprobar datos
    comprobar_dato = () => {
        var form = 'dato-' + i.toString() /* Cojo el formulario */
        dato = document.getElementById(form).value

        if (dato && !isNaN(dato)) {
            dato = parseInt(dato)
            if (dato != -1) {
                lista_datos.push(dato)
                document.getElementById(form).value = ""
                i -= 1
            } else {
                document.getElementById('seguir').removeEventListener('click', siguiente) /* Desacrivar evento */
                document.getElementById('seguir').setAttribute('class', 'desactivate') /* Ocultar boton */
                document.getElementById('output').setAttribute('class', 'container code mt-2') /* Mostrar salida */
                document.getElementById('date').setAttribute('class', 'desactivate') /* Desactivamos */
                document.getElementById('explicar').setAttribute('class', 'btn botonBlue') /* Mostrar boton explicar */
                document.getElementById('explicar').addEventListener('click', explicacion) /* COgemos el elemento le agregamos la función click */
                salida()
            }

        } else {
            i--
            alertify.error('Debe ingresar un valor para continuar')
        }
    }

    // Siguiente
    siguiente = () => {
        i++
        comprobar_dato()
    }

    // Ejecutar
    ejecutar = () => { /* La función */
        document.getElementById('ejecutar').removeEventListener('click', ejecutar) /* Eliminamos evento */
        document.getElementById('ejecutar').setAttribute('class', 'desactivate') /* Ocultamos boton */
        document.getElementById('seguir').setAttribute('class', 'btn botonBlue') /* Ocultamos boton */
        document.getElementById('seguir').addEventListener('click', siguiente) /* Agregamos evento */
        document.getElementById('date').setAttribute('class', 'container code mt-2')
    }
    document.getElementById('ejecutar').addEventListener('click', ejecutar) /* COgemos el elemento le agregamos la función click */

    // Empezar
    empezar = () => {
        document.getElementById('enunciado').setAttribute("class", "desactivate")
        document.getElementById('codigo').setAttribute("class", "container row mx-auto mt-5")
    }
    document.getElementById('start').addEventListener('click', empezar)

}())