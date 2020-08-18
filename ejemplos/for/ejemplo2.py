n = int(input("Ingrese el numero n de la suseción: "))
suma = 0
for i in range(1,n+1):
    print("2^",i,"=",2**i)
    suma += 2**i
print("La suma total es: ",suma)