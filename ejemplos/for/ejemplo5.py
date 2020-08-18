n = int(input("Ingrese numero"))
x = 0
y = 1
print(x,y,end=" ")
for i in range(n+1):
    z = x + y
    print(z,end=" ")
    x = y
    y = z

