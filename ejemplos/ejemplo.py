numeros = [1,2,3,4,5]
numeros2 = [6,7,8,9,10]
for x,y in zip(numeros,numeros2):
    numero1 = x
    numeros2 = y
    suma = numero1 + numeros2
    print(x,y,' = ',suma)


