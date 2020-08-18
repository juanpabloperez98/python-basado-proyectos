numero = 0
while(True):
    numero = int(input("Ingresa numero: "))
    if(numero%2 != 0):
        print("Numero impar: ",numero)
    else:
        print("El numero es par, se cerrara el programa")
        break
