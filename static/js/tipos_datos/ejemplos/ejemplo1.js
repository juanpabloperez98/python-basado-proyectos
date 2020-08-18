(function(){
    // Variables globales
    var ejecutar1 = false /* Me sirve para que me ejecute una sola vez la función ejecutar */
    var explicacion1 = false /* Me sirve para que me ejecute una sola vez la función explicacion */
    
    // Explicación
    explicacion = () => { /* La función */
        document.getElementById('explicacion').setAttribute('class','col-lg-5 mt-3 mx-auto bg-light')
        document.getElementById('explicar').removeEventListener('click',explicacion)
        document.getElementById('explicar').setAttribute('class','desactivate')
        document.getElementById('reiniciar').setAttribute('class','btn botonBlue')
    }   
    if(!explicacion1){
        document.getElementById('explicar').addEventListener('click',explicacion) /* COgemos el elemento le agregamos la función click */
        explicacion1 = true
    }        
    // Ejecutar
    ejecutar = () => { /* La función */
        document.getElementById('output').setAttribute('class','container code mt-2')
        document.getElementById('ejecutar').removeEventListener('click',ejecutar) /* Eliminamos evento */
        document.getElementById('ejecutar').setAttribute('class','desactivate')
        document.getElementById('explicar').setAttribute('class','btn botonBlue')

    }
    if(!ejecutar1){
        document.getElementById('ejecutar').addEventListener('click',ejecutar) /* COgemos el elemento le agregamos la función click */
        ejecutar1 = true
    }
    // Empezar
    empezar = () => {
        document.getElementById('enunciado').setAttribute("class","desactivate")
        document.getElementById('codigo').setAttribute("class","container row mx-auto mt-5")
    }
    document.getElementById('start').addEventListener('click',empezar)
}())