lista_palabras = []
for i in range(5):
    palabra = input("Ingrese una palabra: ")
    lista_palabras.append(palabra)
palabra_remplazar = input("Ingrese palabra que quiere reemplazar: ")
if(palabra_remplazar in lista_palabras):
    palabra_nueva = input("Ingrese palabra nueva: ")
    print("Lista de palabras antes: ",lista_palabras)
    for i in range(len(lista_palabras)):
        if(lista_palabras[i] == palabra_remplazar):
            lista_palabras[i] = palabra_nueva
            break
    print("Lista de palabras despues: ",lista_palabras)
else: print("La palabra que desea reemplazar no se encuentra en la lista")