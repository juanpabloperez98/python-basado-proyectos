(function () {
    // Variables globales
    var num_inputs = 0,
        i = 0,
        lista_datos = []

    // Salida
    salida = () => {
        var numeros = [1, 5, 7, 8, 3, 4]
        for (let i = 0; i < numeros.length; i++) {
            const element = numeros[i];
            document.getElementById('salida').innerHTML += "El cuadrado de " + element.toString() + " es: " + (element ** 2).toString() + "<br>"
        }

    }

    explicacion = () => { /* La función */
        document.getElementById('explicacion').setAttribute('class', 'col-lg-5 mt-3 mx-auto bg-light')
        document.getElementById('explicar').removeEventListener('click', explicacion)
        document.getElementById('explicar').setAttribute('class', 'desactivate')
        document.getElementById('reiniciar').setAttribute('class', 'btn botonBlue')
    }

  
    // Ejecutar
    ejecutar = () => { /* La función */
        document.getElementById('ejecutar').removeEventListener('click', ejecutar) /* Eliminamos evento */
        document.getElementById('ejecutar').setAttribute('class', 'desactivate') /* Ocultamos boton */
        salida()
        document.getElementById('output').setAttribute('class', 'container code mt-2') /* Mostrar salida */
        document.getElementById('explicar').setAttribute('class', 'btn botonBlue') /* Mostrar boton explicar */
        document.getElementById('explicar').addEventListener('click', explicacion) /* COgemos el elemento le agregamos la función click */

    }
    document.getElementById('ejecutar').addEventListener('click', ejecutar) /* COgemos el elemento le agregamos la función click */

    // Empezar
    empezar = () => {
        document.getElementById('enunciado').setAttribute("class", "desactivate")
        document.getElementById('codigo').setAttribute("class", "container row mx-auto mt-5")
    }
    document.getElementById('start').addEventListener('click', empezar)

}())