x = 0 
y = 1 
i = 0
n = int(input("Ingrese un numero: "))
print(x,y,end=" ")
while(i != n+1):
    z = x + y
    print(z,end=" ")
    x = y
    y = z
    i += 1