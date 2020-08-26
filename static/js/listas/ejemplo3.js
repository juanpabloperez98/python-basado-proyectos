(function () {
    // Variables globales
    var num_inputs = 3,
        i = 0,
        pos = 0,
        lista_datos = [],
        lista_palabras = [],
        encontrado = false


        // Salida
        salida = () => {
            palabra_remplazar = lista_datos[0]
            nueva_palabra = lista_datos[1]
            lista_anterior = lista_palabras

            document.getElementById('salida').innerHTML = "Lista de palabras antes: " + lista_palabras


            for (let i = 0; i < lista_palabras.length; i++) {
                const element = lista_palabras[i];
                if (element == palabra_remplazar) {
                    lista_palabras[i] = nueva_palabra
                    encontrado = true
                }
            }

            if (encontrado == false) {
                document.getElementById('salida').innerHTML = "La palabra que desea reemplazar no se encuentra en la lista"
            } else {
                // document.getElementById('salida').innerHTML = "Lista de palabras antes: " + lista_anterior
                document.getElementById('salida').innerHTML += "<br>Lista de palabras despues: " + lista_palabras
            }
        }

    explicacion = () => { /* La función */
        document.getElementById('explicacion').setAttribute('class', 'col-lg-5 mt-3 mx-auto bg-light')
        document.getElementById('explicar').removeEventListener('click', explicacion)
        document.getElementById('explicar').setAttribute('class', 'desactivate')
        document.getElementById('reiniciar').setAttribute('class', 'btn botonBlue')
    }

    fucion_ayuda = (dato, form) => {
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
        if (dato) {
            // dato = parseInt(dato)
            if (i == 1) {
                if (pos == 4) {
                    lista_palabras.push(dato)
                    document.getElementById(form).parentNode.setAttribute('class', 'desactivate')
                    document.getElementById(parent).setAttribute('class', 'form-group')
                } else {
                    lista_palabras.push(dato)
                    document.getElementById(form).value = ""
                    pos++
                    i--
                }
            } else if (i != 1) {
                if (i == 2) {
                    fucion_ayuda(dato, form)
                    for (let i = 0; i < lista_palabras.length; i++) {
                        const element = lista_palabras[i];
                        if (element == lista_datos[0]) {
                            encontrado = true
                        }
                    }

                    console.log(encontrado)


                    if(!encontrado){
                        i = num_inputs
                        lista_datos.push("")
                    }
                }else{
                    fucion_ayuda(dato, form)
                }
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