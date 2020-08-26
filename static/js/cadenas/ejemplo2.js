(function () {
    // Variables globales
    var num_inputs = 1,
        i = 0,
        lista_datos = []

    // Salida
    salida = () => {
        frase = lista_datos[0]
        if (frase.length < 4) {
            document.getElementById('salida').innerHTML = "**Longitud menor a 4**"
        } else if (frase.length > 15) {
            document.getElementById('salida').innerHTML = "**Longitud mayor a 15**"
        } else {
            document.getElementById('salida').innerHTML = "El nombre de usuario es: " + frase
            document.getElementById('seguir').removeEventListener('click', siguiente) /* Desacrivar evento */
            document.getElementById('seguir').setAttribute('class', 'desactivate') /* Ocultar boton */
            document.getElementById('date').setAttribute('class', 'desactivate') /* Desactivamos */
            document.getElementById('explicar').setAttribute('class', 'btn botonBlue') /* Mostrar boton explicar */
            document.getElementById('explicar').addEventListener('click', explicacion) /* COgemos el elemento le agregamos la función click */
        }
        lista_datos.pop()
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

        if (dato) {
            // dato = parseInt(dato)

            lista_datos.push(dato)
            document.getElementById(form).value = ""
            document.getElementById('output').setAttribute('class', 'container code mt-2') /* Mostrar salida */
            i -= 1
            salida()


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