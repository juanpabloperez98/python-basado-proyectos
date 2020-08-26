lista = ["avion", "yate", "tren", "automovil", "motocicleta"]
palabra_eliminar = input("Ingrese que palabra desea eliminar: ")
if (palabra_eliminar in lista):
    lista.remove(palabra_eliminar)
    print("Elemento eliminado: ",lista)
else: print("La palabra que desea eliminar no esta en la lista")
