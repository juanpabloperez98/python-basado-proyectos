n = int(input("Ingrese el orden de la matriz: "))
if(n >= 2 and n <= 5):
    for filas in range(n):
        for columnas in range(n):
            print("| %d-%d |" % (filas,columnas), end="")
        print("\n")
else: print("Orden de la matriz no valido")