(function () {
    // Variables globales
    var num_inputs = 2,
        i = 0,
        lista_datos = []

    // Salida
    salida = () => {
        cadena = lista_datos[0]
        numero = lista_datos[1]

        if(numero > cadena.length  || numero < 0){
            document.getElementById('salida').innerHTML = "Indice erroneo"
        }else{
            document.getElementById('salida').innerHTML = "El caracter ubicado en esa posición es: " + cadena[numero]
        }

    }

    explicacion = () => { /* La función */
        document.getElementById('explicacion').setAttribute('class', 'col-lg-5 mt-3 mx-auto bg-light')
        document.getElementById('explicar').removeEventListener('click', explicacion)
        document.getElementById('explicar').setAttribute('class', 'desactivate')
        document.getElementById('reiniciar').setAttribute('class', 'btn botonBlue')
    }

    fucion_ayuda = (dato,form) => {
        lista_datos.push(dato)
        document.getElementById(form).parentNode.setAttribute('class', 'desactivate')
        if (i != num_inputs) {
            document.getElementById(parent).setAttribute('class', 'form-group')
        }
    }

    // Comprobar datos
    comprobar_dato = () => {
        var form = 'dato-' + i.toString() /* Cojo el formulario */
        parent = 'parent-' + i.toString()
        dato = document.getElementById(form).value
        if (dato && !isNaN(dato)) {
            dato = parseInt(dato)
            fucion_ayuda(dato,form)
        } else {
            if (dato) {
                fucion_ayuda(dato,form)
            }else{
                i--
                alertify.error('Debe ingresar un valor para continuar')
            }
        }
    }

    // Siguiente
    siguiente = () => {
        i++

        comprobar_dato()

        if (i == num_inputs) {
            document.getElementById('seguir').removeEventListener('click', siguiente) /* Desacrivar evento */
            document.getElementById('seguir').setAttribute('class', 'desactivate') /* Ocultar boton */
            document.getElementById('output').setAttribute('class', 'container code mt-2') /* Mostrar salida */
            document.getElementById('date').setAttribute('class', 'desactivate') /* Desactivamos */
            document.getElementById('explicar').setAttribute('class', 'btn botonBlue') /* Mostrar boton explicar */
            document.getElementById('explicar').addEventListener('click', explicacion) /* COgemos el elemento le agregamos la función click */
            salida()
        }

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