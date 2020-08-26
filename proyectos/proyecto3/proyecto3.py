#parte 8
def ver_prestamos(prestamos):
    print("***Prestamos realizados***")
    for i in prestamos:
        print("Nombre: ",i['nombre'])
        print("Cedula: ",i['cedula'])
        print("Fecha del prestamo: ",i['prestamos'])
        print("Fecha de devolucion: ",i['devolucion'])
        print("Libro: ",i['libro']['titulo'])

#parte 7
def ver_libros(libros):
    print("***Libros disponibles***")
    for i in libros:
        print("isbn",i['isbn'])
        print("titulo",i['titulo'])
        print("autor",i['autor'])
        print("copias disponibles",i['copias'])

#parte 6
def eliminar_libros(libros):
    isbn = int(input("Ingrese ISBN: "))
    indice = -1
    for i in range(len(libros)):
        if(libros[i]['isbn'] == isbn):indice = i
    if (indice != -1):
        libros.pop(indice)
        print("**Libro eliminado con exito**")
    else:print("**Libro no encontrado intente de nuevo**")
    return libros

# Parte 5
def prestamo(libros,prestamos):
    isbn = int(input("Ingrese isbn del libro a prestar: "))
    libro = buscar_libro(libros,isbn)
    if(libro != None):
        if(libro['copias'] > 0):
            nombre = input("Ingrese nombre del usuario: ")
            cc = int(input("Ingrese documento: "))
            fecha_prestamo = input("Ingrese la fecha prestamo: (dd/mm/año)")
            fecha_devolución = input("Ingrese la fecha devolución: (dd/mm/año)")
            libro['copias'] -= 1
            prestamo = dict(nombre = nombre, cedula = cc, prestamos = fecha_prestamo, devolucion = fecha_devolución, libro = libro)
            prestamos.append(prestamo)
            print("**Prestamo realizado con exito**")
        else:print("El libro no tiene copias disponibles")
    else:print("No existe libro")
    return prestamos, libros

# Parte 4
def crear_libro(libros):
    libro = None
    isbn = int(input("Ingrese ISBN: "))
    libro = buscar_libro(libros,isbn)            
    if(libro == None):
        titulo = input("Ingrese titulo del libro: ")
        autor = input("Autor del libro: ")
        copias = int(input("Numero de copias disponibles: "))
        libro = dict(isbn = isbn, titulo = titulo, autor = autor, copias = copias)
        libros.append(libro)
        print("**Libro creado con exito**")
    else:print("\nEl libro que intenta crear ya esta creado, intentelo de nuevo\n")
    return libros

# Parte 3
def buscar_libro(libros,isbn):
    for i in libros:
        if(i['isbn'] == isbn): return i
    return None

# Parte 2
def menu():
    print("***Menu biblioteca***")
    print("1)Crear libro")
    print("2)Prestar libro")
    print("3)Eliminar libro")
    print("4)Ver libros")
    print("5)Ver Prestamos")
    print("6)Salir")

# Parte 1
def main():
    libros = []
    prestamos = []
    while(True):
        menu()
        op = int(input("Ingrese una opcion: "))
        if(op==1):libros = crear_libro(libros)
        elif(op==2):prestamos,libros = prestamo(libros,prestamos)
        elif(op==3):libros = eliminar_libros(libros)
        elif(op==4):ver_libros(libros)
        elif(op==5):ver_prestamos(prestamos)
        elif(op==6):
            print("\nHasta luego\n")
            break
        else:print("\nOpción no valida\n")

main()