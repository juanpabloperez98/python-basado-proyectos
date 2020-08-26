num_veces = int(input("Ingrese el numero de veces que desea ingresar palabras: "))
lista_palabras = []
for i in range(num_veces):
    palabra = input("Digite la palabra {}:".format(i))
    lista_palabras.append(palabra)
palabra_buscar = input("Ingrese palabra a buscar: ")
con = 0
for i in lista_palabras:
    if(i == palabra_buscar): con += 1
if(con > 0): print("La palabara aparece {}".format(con))
else: print("La palabra no se encuentra en la lista")