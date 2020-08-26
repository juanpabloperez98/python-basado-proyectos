lista_materias = []
while(True):
    materia = input("Ingrese una materia: ")
    lista_materias.append(materia)
    longitud = len(lista_materias)
    if(longitud >= 3): break
print("Lista de materias: ",lista_materias)