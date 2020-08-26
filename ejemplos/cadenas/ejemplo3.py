cadena = input("Ingrese una cadena de caracteres: ")
mayusculas = 0
minusculas = 0
digitos = 0
for i in cadena:
    if(i.islower()): minusculas += 1
    elif(i.isupper()): mayusculas +=1
    elif(i.isnumeric()): digitos += 1
print("Numero de mayusculas: %d Numero de minusculas: %d Numero de digitos: %d" % (mayusculas,minusculas,digitos))