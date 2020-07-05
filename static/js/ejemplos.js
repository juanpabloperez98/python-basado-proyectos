prompt
array.push()
array.concat()
array.join(" : ")
array.sort()
array.reverse()
document.getElementsByTagName("div")

// ---------------------------------------------------------------


var elemento = document.createElement("h1")
var contenido = document.createTextNode("Este es el texto")

elemento.appendChild(contenido)

elemento.setAttribute("class","bg-dark")

document.getElementById("botones").appendChild(elemento)

// ---------------------------------------------------------------

var elemento = document.createElement("li")
var contenido = document.createTextNode("Este es el nuevo li")

elemento.appendChild(contenido)


var padre = document.getElementsByTagName("li")[2].parentNode,
    hijo = document.getElementsByTagName("li")[2]


padre.appendChild(elemento)

padre.insertBefore(elemento,hijo)

// ---------------------------------------------------------------