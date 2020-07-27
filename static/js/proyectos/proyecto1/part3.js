(function () {

    var cont = 0
        sta_regis_open = 0
        sta_main_open = 0

    /* SEGUNDO CODIGO */
    var valores2 = {
        1:4
    }
    numero_parada2 = 1

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
            document.getElementById('reiniciar2').setAttribute('class','btn botonYellow') /* Cambio de color */
            
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
            $('#' + contador_actual).toggle("fold")
            $('#' + contador_siguient).toggle("explode")
            document.getElementById('siguiente').setAttribute('class', 'desactivate') /* Oculto el boton siguient */
            document.getElementById('probar').setAttribute('class', 'btn botonYellow') /* Muestro el boton probar */
            document.getElementById('reiniciar').setAttribute('class','btn botonBlue') /* Cambio de color */
        }else{
            $('#new-employee').toggle("fold")            
            $('#explicacion2').toggle("fold")
            $('#main').toggle("fold")
            $('#botones-1').toggle("fold")
            document.getElementById('botones-register').setAttribute('class','')


            document.getElementById('part').setAttribute('class','nav-item')
            document.getElementById('siguiente-ejercicio').setAttribute('class','text-center col-lg-12 mx-auto my-5')
            // document.getElementById('new-employee').setAttribute('class','container code text-justify mt-2') /* Desactivo el codigo de la función */
            // document.getElementById('main').setAttribute('class','desactivate') /* Activo el codigo main  */
            // document.getElementById('explicacion2').setAttribute('class','desactivate') /* Activo las opciones del segundo codigo */
            // document.getElementById('botones-1').setAttribute('class','')
        }
    }


    // Muestra la explicación del Register
    var ExplicarRegister = () => {
        // document.getElementById('explicacionCode1').setAttribute('class','col-lg-6 mt-3 mx-auto bg-light')        
        $('#explicacionCode1').toggle('explode')
        $('#botones-register').toggle('explode')
        sta_regis_open = 1
    }

    // Muestra la explicación de Main
    var ExplicarMain = () => {
        // document.getElementById('explicacionCode1').setAttribute('class','col-lg-6 mt-3 mx-auto bg-light')        
        $('#explicacionCode2').toggle('explode')
        $('#botones-main').toggle('explode')
        sta_main_open = 1
    }

    // Sirve para mostrar el codigo del main
    var ShowMainCode = () =>{
        $('#main').toggle('explode')
        $('#botones-main').toggle('explode')
        $('#new-employee').toggle('explode')
        document.getElementById('btn-registrar_nuevo').setAttribute('class','btn botonBlue')
        document.getElementById('btn-main').setAttribute('class','desactivate')        
        if(sta_regis_open == 1){
            ExplicarRegister()                
            sta_regis_open = 0
        }
    }

    var ShowRegisterCode = () => {
        $('#main').toggle('explode')
        $('#botones-main').toggle('explode')
        $('#new-employee').toggle('explode')
        document.getElementById('btn-registrar_nuevo').setAttribute('class','desactivate')
        document.getElementById('btn-main').setAttribute('class','btn botonBlue')        
        if(sta_main_open == 1){
            ExplicarMain()
            sta_main_open = 0
        }

    }



    /* PRIMER CODIGO */
    numero_parada = 5
    valores = {
        1: 3,
        2: 4,
        3: 2,
        4: 3,
        5: 1,
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
            // Vamos a la parte 2
            part = 2            
            $('#new-employee').toggle("fold")
            $('#main').toggle("explode")
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

    document.getElementById('explicarregister').addEventListener('click',ExplicarRegister)
    document.getElementById('explicarmain').addEventListener('click',ExplicarMain)
    document.getElementById('btn-main').addEventListener('click',ShowMainCode)
    document.getElementById('btn-registrar_nuevo').addEventListener('click',ShowRegisterCode)


}())


