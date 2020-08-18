nota = 0
suma_notas = 0
numero_notas = 0
while(nota != -1):
    nota = int(input("Ingrese nota: "))
    suma_notas += nota
    numero_notas += 1
promedio = suma_notas/numero_notas
print("Promedio es: ",(promedio))