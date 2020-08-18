numero_anterior = 0
while(True):
    numero = int(input("Ingrese un numero: "))
    print("Numero ingresado es: ",numero)
    if(numero_anterior > numero):
        print("Numero menor al anterior")
        break
    else:numero_anterior = numero