(function () {

    var cont = 0
    sta_1_open = 0
    sta_2_open = 0
    sta_3_open = 0
    status = 1

    /* Tercer codigo */

    var valores3 = {
        1: 3,
        2: 2,
    }
    numero_parada3 = 2

    var probar3 = () => {
        cont++ /* Aumentamos contador */
        if (cont < 7) {
            var id_select = 's3-' + cont.toString() /* Concatenamos el id correspondiente */

            var value = document.getElementById(id_select).selectedIndex /* Escogemos el box del select con el id correspondiente */
            if (value != 0) { /* Valido que haya escojido una opción del select */
                validar3(value)
            } else {
                alertify.error("Escoja una opción") /* Imprimimos que el usuario no escojio ningun error */
                cont-- /* Disminuimos el contador */
            }
        }
    }

    const validar3 = (op) => {
        if (valores3[cont] == op) {
            // alertify.success('Felicitaciones<br>La linea correcta')
            var sel = 'sel3-' + cont.toString() /* Genero cadena para el id de la sección de selección */
            var exp = 'exp3-' + cont.toString() /* Genero la cadena del id  para la sección de explicación que es la que viene despues de dar probar */
            $('#' + exp).toggle("fold")
            $('#' + sel).toggle("explode")
            agregar_codigo3() /* Llamo a la función que me agrega el codigo */
            document.getElementById('siguiente3').setAttribute('class', 'btn botonBlue') /* Muestro el boton siguiente */
            document.getElementById('probar3').setAttribute('class', 'desactivate') /* Oculto el boton  probar*/
            document.getElementById('reiniciar3').setAttribute('class', 'btn botonYellow') /* Cambio de color */

        } else {
            alertify.error("¿Estas seguro?<br>Revisa nuevamente")
            cont--
        }
    }

    const agregar_codigo3 = () => {
        var linea = '3l' + cont.toString() /* Creo el string respectivo */
        var code = '3l-' + cont.toString()
        var linea_code = document.getElementById(linea) /* Cojo el elemento */
        var code = document.getElementById(code)
        linea_code.setAttribute('class', '') /* Le quito el sombreado gris */
        code.setAttribute('class', '') /* Muestro la linea de codigo */
    }

    var siguiente3 = () => {


        if (cont != numero_parada3) { /* Validamos que no se haya llegado a la ultima linea */
            contador_actual = cont.toString() /* Convierto a string el contador actual */
            contador_siguient = (cont + 1).toString() /* Convierto a string el contador siguiente */

            contador_actual = 'd3-' + contador_actual
            contador_siguient = 'd3-' + contador_siguient


            $('#' + contador_actual).toggle("fold")
            $('#' + contador_siguient).toggle("explode")

            document.getElementById('siguiente3').setAttribute('class', 'desactivate') /* Oculto el boton siguient */
            document.getElementById('probar3').setAttribute('class', 'btn botonYellow') /* Muestro el boton probar */
            document.getElementById('reiniciar3').setAttribute('class', 'btn botonBlue') /* Cambio de color */
        } else {
            $('#new-employee').toggle("fold")
            $('#explicacion3').toggle("fold")
            $('#main').toggle("fold")
            $('#botones-1').toggle("fold")
            document.getElementById('botones-nomina').setAttribute('class', '')
            document.getElementById('part').setAttribute('class', 'nav-item')
            document.getElementById('siguiente-ejercicio').setAttribute('class', 'text-center col-lg-12 mx-auto my-5')
            status = 1
        }
    }


    const Explicar1 = () => {
        $('#explicacionCode1').toggle('explode')
        $('#botones-nomina').toggle('explode')
        sta_1_open = 1
    }

    const Explicar2 = () => {
        $('#explicacionCode2').toggle('explode')
        $('#botones-boni').toggle('explode')
        sta_2_open = 1
    }

    const Explicar3 = () => {
        $('#explicacionCode3').toggle('explode')
        $('#botones-main').toggle('explode')
        sta_3_open = 1
    }

    var ShowCode1 = () => {
        if (status == 3) {
            $('#main').toggle('explode')
            $('#botones-main').toggle('explode')
        } else if (status == 2) {
            $('#new-employee2').toggle('explode')
            $('#botones-boni').toggle('explode')
        }

        if (sta_2_open == 1) {
            Explicar2()
            sta_2_open = 0
        } else if (sta_3_open == 1) {
            Explicar3()
            sta_3_open = 0
        }

        $('#new-employee').toggle('explode')
        $('#botones-nomina').toggle('explode')

        document.getElementById('btn-pagarnomina').setAttribute('class', 'desactivate')
        document.getElementById('btn-main').setAttribute('class', 'btn botonBlue')
        document.getElementById('btn-bonificaciones').setAttribute('class', 'btn botonBlue')
        status = 1

    }

    var ShowCode2 = () => {
        if (status == 3) {
            $('#main').toggle('explode')
            $('#botones-main').toggle('explode')
        } else if (status == 1) {
            $('#new-employee').toggle('explode')
            $('#botones-nomina').toggle('explode')
        }

        if (sta_1_open == 1) {
            Explicar1()
            sta_1_open = 0
        } else if (sta_3_open == 1) {
            Explicar3()
            sta_3_open = 0
        }

        $('#new-employee2').toggle('explode')
        $('#botones-boni').toggle('explode')

        document.getElementById('btn-bonificaciones').setAttribute('class', 'desactivate')
        document.getElementById('btn-main').setAttribute('class', 'btn botonBlue')
        document.getElementById('btn-pagarnomina').setAttribute('class', 'btn botonBlue')

        status = 2

    }

    var ShowCode3 = () => {
        if (status == 1) {
            $('#new-employee').toggle('explode')
            $('#botones-nomina').toggle('explode')
        } else if (status == 2) {
            $('#new-employee2').toggle('explode')
            $('#botones-boni').toggle('explode')
        }

        if (sta_2_open == 1) {
            Explicar2()
            sta_2_open = 0
        } else if (sta_1_open == 1) {
            Explicar1()
            sta_1_open = 0
        }

        $('#main').toggle('explode')
        $('#botones-main').toggle('explode')

        document.getElementById('btn-main').setAttribute('class', 'desactivate')
        document.getElementById('btn-pagarnomina').setAttribute('class', 'btn botonBlue')
        document.getElementById('btn-bonificaciones').setAttribute('class', 'btn botonBlue')

        status = 3

    }


    /* SEGUNDO CODIGO */
    var valores2 = {
        1: 3,
        2: 1,
        3: 1,
        4: 4,
        5: 1,
    }
    numero_parada2 = 5

    var probar2 = () => {
        cont++ /* Aumentamos contador */
        if (cont < 7) {
            var id_select = 's2-' + cont.toString() /* Concatenamos el id correspondiente */

            var value = document.getElementById(id_select).selectedIndex /* Escogemos el box del select con el id correspondiente */
            if (value != 0) { /* Valido que haya escojido una opción del select */
                validar2(value)
            } else {
                alertify.error("Escoja una opción") /* Imprimimos que el usuario no escojio ningun error */
                cont-- /* Disminuimos el contador */
            }
        }
    }

    const validar2 = (op) => {
        if (valores2[cont] == op) {
            // alertify.success('Felicitaciones<br>La linea correcta')
            var sel = 'sel2-' + cont.toString() /* Genero cadena para el id de la sección de selección */
            var exp = 'exp2-' + cont.toString() /* Genero la cadena del id  para la sección de explicación que es la que viene despues de dar probar */
            $('#' + exp).toggle("fold")
            $('#' + sel).toggle("explode")
            agregar_codigo2() /* Llamo a la función que me agrega el codigo */
            document.getElementById('siguiente2').setAttribute('class', 'btn botonBlue') /* Muestro el boton siguiente */
            document.getElementById('probar2').setAttribute('class', 'desactivate') /* Oculto el boton  probar*/
            document.getElementById('reiniciar2').setAttribute('class', 'btn botonYellow') /* Cambio de color */

        } else {
            alertify.error("¿Estas seguro?<br>Revisa nuevamente")
            cont--
        }
    }

    const agregar_codigo2 = () => {
        var linea = '2l' + cont.toString() /* Creo el string respectivo */
        var code = '2l-' + cont.toString()
        var linea_code = document.getElementById(linea) /* Cojo el elemento */
        var code = document.getElementById(code)
        linea_code.setAttribute('class', '') /* Le quito el sombreado gris */
        code.setAttribute('class', '') /* Muestro la linea de codigo */
    }

    var siguiente2 = () => {


        if (cont != numero_parada2) { /* Validamos que no se haya llegado a la ultima linea */
            contador_actual = cont.toString() /* Convierto a string el contador actual */
            contador_siguient = (cont + 1).toString() /* Convierto a string el contador siguiente */

            contador_actual = 'd2-' + contador_actual
            contador_siguient = 'd2-' + contador_siguient


            $('#' + contador_actual).toggle("fold")
            $('#' + contador_siguient).toggle("explode")

            document.getElementById('siguiente2').setAttribute('class', 'desactivate') /* Oculto el boton siguient */
            document.getElementById('probar2').setAttribute('class', 'btn botonYellow') /* Muestro el boton probar */
            document.getElementById('reiniciar2').setAttribute('class', 'btn botonBlue') /* Cambio de color */
        } else {
            $('#new-employee2').toggle("fold")
            $('#explicacion2').toggle("fold")
            $('#main').toggle("fold")
            $('#explicacion3').toggle("fold")
            cont = 0
            // document.getElementById('botones-register').setAttribute('class','')


            // document.getElementById('part').setAttribute('class','nav-item')
            // document.getElementById('siguiente-ejercicio').setAttribute('class','text-center col-lg-12 mx-auto my-5')
            // document.getElementById('new-employee').setAttribute('class','container code text-justify mt-2') /* Desactivo el codigo de la función */
            // document.getElementById('main').setAttribute('class','desactivate') /* Activo el codigo main  */
            // document.getElementById('explicacion2').setAttribute('class','desactivate') /* Activo las opciones del segundo codigo */
            // document.getElementById('botones-1').setAttribute('class','')
        }
    }




    /* PRIMER CODIGO */
    numero_parada = 5
    valores = {
        1: 3,
        2: 4,
        3: 1,
        4: 2,
        5: 3,
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
            document.getElementById('reiniciar').setAttribute('class', 'btn botonBlue') /* Cambio de color */

        } else {
            // Vamos a la parte 2
            part = 2

            $('#new-employee').toggle("fold")
            $('#new-employee2').toggle("fold")
            $('#explicacion').toggle("fold")
            $('#explicacion2').toggle("explode")
            cont = 0
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
            document.getElementById('reiniciar').setAttribute('class', 'btn botonYellow') /* Cambio de color */


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


    // Añadir eventos de la parte 2
    document.getElementById('probar2').addEventListener('click', probar2)
    document.getElementById('siguiente2').addEventListener('click', siguiente2)


    // Añadir eventos de la parte 3
    document.getElementById('probar3').addEventListener('click', probar3)
    document.getElementById('siguiente3').addEventListener('click', siguiente3)


    // Eventos finales
    document.getElementById('explicar1').addEventListener('click', Explicar1)
    document.getElementById('explicar2').addEventListener('click', Explicar2)
    document.getElementById('explicar3').addEventListener('click', Explicar3)


    document.getElementById('btn-pagarnomina').addEventListener('click', ShowCode1)
    document.getElementById('btn-bonificaciones').addEventListener('click', ShowCode2)
    document.getElementById('btn-main').addEventListener('click', ShowCode3)





}())


