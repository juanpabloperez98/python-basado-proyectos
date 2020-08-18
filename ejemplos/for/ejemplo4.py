n = int(input("Ingrese un numero: "))
numeropares = 0
for i in range(1,n+1):
    if(i%2 == 0):
        print("Numero %d es par" % i)
        numeropares += 1
print("Numero de pares totales encontrados: ",numeropares)