(function () {

    var cont = 0
    numero_parada = 3
    valores = {
        1: 1,
        2: 3,
        3: 2,
    }

    // Evento explicar
    var explicar = () => {
        document.getElementById('explicacionCode').setAttribute('class','col-lg-5 mt-3 mx-auto bg-light')
        document.getElementById('explicar').setAttribute('class','desactivate')
        document.getElementById('siguiente-ejercicio').setAttribute('class','text-center col-lg-12 mx-auto my-5')
        document.getElementById('part2').setAttribute('class','nav-item')
    }
    // Función que me agrega al codigo la linea selecciónada
    const agregar_codigo = () => {
        var linea = 'l' + cont.toString() /* Creo el string respectivo */
        var code = 'l-' + cont.toString()
        var linea_code = document.getElementById(linea) /* Cojo el elemento */
        var code = document.getElementById(code)
        linea_code.setAttribute('class', '') /* Le quito el sombreado gris */
        code.setAttribute('class', '') /* Muestro la linea de codigo */
    }
    // Función siguiente
    var siguiente = () => {
        if (cont != numero_parada) { /* Validamos que no se haya llegado a la ultima linea */
            contador_actual = cont.toString() /* Convierto a string el contador actual */
            contador_siguient = (cont + 1).toString() /* Convierto a string el contador siguiente */
            $('#' + contador_actual).toggle("fold")
            $('#' + contador_siguient).toggle("explode")
            document.getElementById('siguiente').setAttribute('class', 'desactivate') /* Oculto el boton siguient */
            document.getElementById('probar').setAttribute('class', 'btn botonYellow') /* Muestro el boton probar */
            document.getElementById('reiniciar').setAttribute('class','btn botonBlue') /* Cambio de color */
        }else{
            document.getElementById('explicacion').setAttribute('class','desactivate')
            document.getElementById('botones-1').setAttribute('class','')


        }
    }
    // Función validar (Cuando se le de click al boton probar)
    const validar = (op) => {
        if (valores[cont] == op) {
            // alertify.success('Felicitaciones<br>La linea correcta')
            var sel = 'sel-' + cont.toString() /* Genero cadena para el id de la sección de selección */
            var exp = 'exp-' + cont.toString() /* Genero la cadena del id  para la sección de explicación que es la que viene despues de dar probar */
            $('#' + exp).toggle("fold")
            $('#' + sel).toggle("explode")
            agregar_codigo() /* Llamo a la función que me agrega el codigo */
            document.getElementById('siguiente').setAttribute('class', 'btn botonBlue') /* Muestro el boton siguiente */
            document.getElementById('probar').setAttribute('class', 'desactivate') /* Oculto el boton  probar*/
            document.getElementById('reiniciar').setAttribute('class','btn botonYellow') /* Cambio de color */
        } else {
            alertify.error("¿Estas seguro?<br>Revisa nuevamente")
            cont--
        }
    }
    // Evento probar
    var probar = () => {
        cont++ /* Aumentamos contador */
        if (cont < 7) {
            var id_select = 's-' + cont.toString() /* Concatenamos el id correspondiente */
            console.log(cont)
            var value = document.getElementById(id_select).selectedIndex /* Escogemos el box del select con el id correspondiente */
            if (value != 0) { /* Valido que haya escojido una opción del select */
                validar(value)
            } else {
                alertify.error("Escoja una opción") /* Imprimimos que el usuario no escojio ningun error */
                cont-- /* Disminuimos el contador */
            }
        }
    }
    // Evento empezar el ejercicio
    var go = () => {
        document.getElementById('statment').setAttribute('class', 'desactivate')
        document.getElementById('codigo').setAttribute('class', 'container row mx-auto mt-5')
    }
    // Añadir eventos
    document.getElementById('go').addEventListener('click', go)
    document.getElementById('probar').addEventListener('click', probar)
    document.getElementById('siguiente').addEventListener('click', siguiente)
    document.getElementById('explicar').addEventListener('click',explicar)
}())
