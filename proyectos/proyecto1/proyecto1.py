"""  
Sistema de nominas:
Se desea realizar un sistema de nominas para una empresa de venta de carros, el cual consiste en llevar un registro
de los empleados que tiene la empresa, los trabajos realizados por el empleado, y las bonificaciones que tiene cada empleado

El software debe tener un menu que le permita al administrador del programa poder hacer las siguiente tareas:
-Registrar un nuevo empleado.
-Eliminar un empleado.
-Pagar nomina.
-Pagar bonificaciones.
-ver detalles del empleado   
-Venta de un carro

*Al momento de correr el programa debe pedir el capital de nomina con el que se va a trabajar
*Al momento de registrar un nuevo empleado se pediran (cc,nombre,apellido,bonificaciones,numero ventas,salario)
*El pago de nomina se realiza basado al salario del empleado, y dependera del capital de nomina que tenga la empresa, dado el caso de que el capital no sea suficiente para pagar la nomina, se debera informar al admin
*El pago de bonificaciones dependera del numero de ventas que haya realizado un empleado,si el numero de ventas de un empleado supera un valor a 2, su bonificacion sera del 20% con respecto a su salario, si es mayor a 4, sera de un 40% con respecto a su salario, se debe disminuir el capital de nomina
*Al pagar bonificaciones, el numero de ventas del empleado se reducira a 0 y las bonificaciones aumentaran a 1
*Ver detalles del empleado, mostrara los detalles del empleado (cc,nombre,apellido,bonificaciones,numero ventas,salario)
*Al vender un carro, la venta del carro sumara al capital de nomina y aumentara el numero de ventas del empleado que vendió el carro
"""
# Parte 1: Crear función principal
# Parte 2: Dibujar el menu
# Parte 3: Registrar empleado
# Parte 4: Eliminar un empleado
# Parte 5: Pagar nomina y bonificaciones
# Parte 6: Ver detalles del empleado
# Parte 7: Venta de un carro

"""  
Temas:
    -Estructuras de secuencia
    -Estructuras condicionales
    -Estructuras repetitivas
    -Estructuras de datos (listas)
    -Funciones
"""

# Parte 1
def main():
    fin = False
    lista_empleados = []
    capital_nomina = int(input("Ingrese el capital de nomina: "))
    while (fin != True):
        menu()
        opcion = int(input("Ingrese una opcion: "))
        if(opcion == 1):
            registrar_nuevo(lista_empleados)
        elif(opcion == 2):
            estado = eliminar_empleado(lista_empleados)
            if(estado == True):
                print("\nEmpleado Eliminado!!\n")
            else:
                print("\nEmpleado No encontrado!!\n")
        elif(opcion == 3):
            estado, capital_nomina = pagarnomina(lista_empleados, capital_nomina)
            if(estado == True):
                print("\nNomina cancelada con exito!!\n")
            else:
                print("\nEl capital no alcanza!!\n")
        elif(opcion == 4):
            estado, capital_nomina = pagarbonificaciones(lista_empleados, capital_nomina)
            if(estado == True):
                print("\Bonificación cancelada con exito!!\n")
            else:
                print("\nLa bonificacion no pudo ser realizada!!\n")
        elif(opcion == 5):
            estado = ver_detalle(lista_empleados)
            if (estado == False):
                print("\nNo se pudo encontrar el empleado\n")
        elif(opcion == 6):
            estado,capital_nomina = venta_carro(lista_empleados,capital_nomina) 
            if(estado == False):
                print("\nNo se pudo encontrar el empleado\nVuelva a intentar")
        elif(opcion == 7):
            print("\nHasta luego\n")
            fin = True
        elif(opcion == 8):
            print("*****", capital_nomina)
            print("-----", lista_empleados)
            
        else:print("\nEscoja una opción correcta\n")
# Parte 2
def menu():
    print("\n---SISTEMA DE NOMINAS---\n")
    print("1)Registrar un nuevo empleado.")
    print("2)Eliminar un empleado.")
    print("3)Pagar nomina.")
    print("4)Pagar bonificaciones.")
    print("5)ver detalles del empleado.")
    print("6)Venta de un carro.")
    print("7)Salir.")

# Parte 3
def registrar_nuevo(lista_empleados):
    cc = int(input("Cedula: "))
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    bonificaciones = 0
    numero_ventas = 0
    salario = int(input("Ingrese el salario $: "))
    datos = [cc, nombre, apellido, bonificaciones, numero_ventas, salario]
    lista_empleados.append(datos)
    
    print("\n***Empleado registrado con exito!!***\n")

# Parte 4
def eliminar_empleado(lista_empleados):
    cc = int(input("Ingrese cedula del empleado: "))
    longitud_lista = len(lista_empleados)
    for i in range(longitud_lista):
        empleado = lista_empleados[i]
        if (empleado[0] == cc):
            lista_empleados.pop(i)
            return True
    return False

# Parte 5
def pagarnomina(lista_empleados, capital_nomina):
    cc = int(input("Ingrese cedula del empleado: "))
    longitud_lista = len(lista_empleados)
    for i in range(longitud_lista):
        empleado = lista_empleados[i]
        if (empleado[0] == cc):
            if(capital_nomina > empleado[5]):
                capital_nomina -= empleado[5]
            else:
                break
            return (True, capital_nomina)
    return (False, capital_nomina)

# Parte 5
def pagarbonificaciones(lista_empleados, capital_nomina):
    cc = int(input("Ingrese cedula del empleado: "))
    longitud_lista = len(lista_empleados)
    for i in range(longitud_lista):
        empleado = lista_empleados[i]
        if (empleado[0] == cc):
            if(empleado[4] > 2 and empleado[4] < 4):
                boni = empleado[5] * 0.20
                if(boni < capital_nomina):
                    empleado[3] += 1
                    empleado[4] = 0
                    return (True, capital_nomina)
                else:
                    print("\nEl capital no es suficiente\n")
                    break
            elif(empleado[4] > 4):
                boni = empleado[5] * 0.40
                if(boni < capital_nomina):
                    empleado[3] += 1
                    empleado[4] = 0
                    return (True, capital_nomina)
                else:
                    print("\nEl capital no es suficiente\n")
                    break
            else:
                print("\nEl empleado no recibe bonificacion\n")
                break
    return (False, capital_nomina)

# Parte 6
def ver_detalle(lista_empleados):
    cc = int(input("Ingrese cedula del empleado: "))
    longitud_lista = len(lista_empleados)
    for i in range(longitud_lista):
        empleado = lista_empleados[i]
        if (empleado[0] == cc):
            print("----EMPLEADO-----")
            print("Cedula: ", empleado[0])
            print("Nombre: ", empleado[1])
            print("Apellido: ", empleado[2])
            print("Bonificaciones pagadas: ", empleado[3])
            print("Numero ventas: ", empleado[4])
            print("Salario: ", empleado[5])
            return True
    return False

# Parte 7
def venta_carro(lista_empleados,capital_nomina):
    cc = int(input("Ingrese cedula del empleado que realizo la venta: "))
    valor = int(input("Ingrese el valor de la venta: "))
    longitud_lista = len(lista_empleados)
    for i in range(longitud_lista):
        empleado = lista_empleados[i]
        if (empleado[0] == cc):
            empleado[4] += 1
            capital_nomina += valor
            print("\nVenta realizada con exito por el empleado ",empleado[1])
            return (True,capital_nomina)
    return (False,capital_nomina)

# Parte 1
main()
