inicio = int(input("Ingrese numero inicio: "))
fin = int(input("Ingrese numero fin: "))
if(inicio < fin):
    suma = 0
    for i in range(inicio,fin):
        suma += i
    print("La suma total es: ",suma)
else: print("Inicio no es menor a fin")