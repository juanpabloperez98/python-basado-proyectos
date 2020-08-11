"""  
Se desea realizar un juego de triqui personalizado para dos jugadores, 
el juego consiste en el tradicional juego de triqui donde el objetivo es que se forme una 
fila, columna o diagonal con las tres fichas de un jugador. 
El juego finaliza cuando uno de los dos jugadores completa o forma una fila, columna o diagonal 
con sus fichas, o cuando se llene todo el tablero, que en este caso será de 3x3 y 
ninguno de los dos jugadores haya ganado el juego. 
"""

"""
Para tener en cuenta:

* Al comenzar el juego, se debe validar si existen jugadores registrados, de lo contrario se le pedirá al usuario que ingrese un nuevo jugador.
* Al crear un nuevo jugador solo se pedirá el nombre del jugador.
* Todos los jugadores tienen un número de partidas ganadas, que irá aumentando cada vez que este jugador gane, por defecto este número de partidas empieza en 0 cada vez que se registre un nuevo jugador.
* Cada vez que se termine una partida, se le debe preguntar al usuario si desea volver a jugar la partida o terminarla.
* Debe haber una opción del menú que permita visualizar los jugadores registrados y el número de partidas ganadas.
* Al terminar la ejecución del programa se debe mostrar en pantalla cuál es el jugador con el mayor número de partidas ganadas.
"""
# Parte 2
def menu():
    print("***MENU***")
    print("1) Empezar juego")
    print("2) Crear jugador")
    print("3) Ver jugadores")
    print("4) Salir")
    print("¿Que opcion desea escoger?")

# Parte 3
def llamada_funciones(op,jugadores):
    if(op == 1):
        jugadores = pedir_datos(jugadores)
    elif(op == 2):
        jugadores = crear_jugador(jugadores)
    elif(op == 3):
        ver_jugadores(jugadores)
    else:
        print("***Opcion no valida***")

# Parte 4
def crear_jugador(jugadores):
    nombre = input("Ingrese nombre del jugador: ")
    for player in jugadores:
        if player['nombre'] == nombre:
            print("Lo sentimos este usuario ya esta registrado")
            return jugadores
    jugador = {'nombre':'','partidas_ganadas':0}
    jugador['nombre'] = nombre
    jugadores.append(jugador)
    print("Jugador %s creado con exito" % (nombre))
    return jugadores 

# Parte 5
def ver_jugadores(jugadores):
    print("****Datos de jugadores****")
    for jugador in jugadores:
        print("---------------------------------------------")
        print("Jugador: ",jugador['nombre'])
        print("Partidas ganadas:",jugador['partidas_ganadas'])
        print("---------------------------------------------")

# Parte 6
def pedir_datos(jugadores):
    if(len(jugadores)>1):
        j1,j2 = escoger_jugadores(jugadores)
        if(j1 != 0 and j2 != 0):
            j1,j2 = escoger_ficha(j1,j2)
            if(j1 != 0 and j2 != 0):
                j1,j2 = empezar_juego(j1,j2)
                for jugador in jugadores:
                    if jugador['nombre'] == j1['nombre']:
                        jugador = j1
                    elif(jugador['nombre'] == j2['nombre']):
                        jugador = j2
                return jugadores
    else:
        print("***No hay jugadores suficientes***")

# Parte 7
def escoger_jugadores(jugadores):
    print("---Jugadores---")
    i = 0
    for jugador in jugadores:
        print(str(i) +  "-" + jugador['nombre'])
        i+=1
    j1 = int(input("Jugador 1 ingrese el numero del jugador a elegir: "))
    j2 = int(input("Jugador 2 ingrese el numero del jugador a elegir: "))
    if(j1 != j2):
        jugador1 = jugadores[j1]
        jugador2 = jugadores[j2]
        return jugador1, jugador2 
    else:
        print("***Los jugadores no pueden ser iguales***")
        return 0,0

# Parte 8
def escoger_ficha(j1,j2):
    lista_fichas = ['*','@','$','&']
    print("***Fichas disponibles***")
    for ficha in range(len(lista_fichas)):
        print(str(ficha),lista_fichas[ficha])
    ficha1 = int(input("Jugador 1 ingrese que ficha desea utilizar:"))    
    ficha2 = int(input("Jugador 2 ingrese que ficha desea utilizar:"))
    if(ficha1 != ficha2):
        j1['ficha'] = lista_fichas[ficha1]
        j2['ficha'] = lista_fichas[ficha2] 
        return j1, j2 
    else:
        print("***Los jugadores no pueden tener la misma ficha***")
        return 0,0 

# Parte 9
def empezar_juego(j1,j2):
    posiciones = [0,1,2,3,4,5,6,7,8]
    turno = 1
    while(True):
        if(turno == 1): print("Jugador1: %s" % j1['nombre'])
        else: print("Jugador2: %s" % j2['nombre'])
        pintar_tablero(posiciones)
        ganador = validar_ganador(j1,j2,posiciones)
        if(ganador != 0):
            if(ganador == 1):
                print("El ganador es: %s" % j1['nombre'])
                j1['partidas_ganadas'] += 1
            if(ganador == 2):
                print("El ganador es: %s" % j2['nombre'])
                j2['partidas_ganadas'] += 1
            if(ganador == 3):
                print("Ningun jugador ha ganado")
            return j1,j2
        t = int(input("Ingrese posicion: "))
        if((t >= 0 and t <= 8) and (posiciones[t] != j1['ficha'] and posiciones[t] != j2['ficha'])):
                if(turno == 1): posiciones[t] = j1['ficha']
                else: posiciones[t] = j2['ficha']
        else: print("Posicion no permitida...Pierde turno")
        if(turno == 1): turno = 2
        else:turno = 1
        
# Parte 10
def pintar_tablero(posiciones):    
    indice = 0
    for i in range(3):
        print("---------------")
        for j in range(3):
            print("| {} |".format(posiciones[indice]),end="")
            indice +=1
        print("")        
    print("---------------")

# Parte 11
def validar_ganador(j1,j2,posiciones):
    ficha1 = j1['ficha']
    if(posiciones[0]==ficha1 and posiciones[3]==ficha1 and posiciones[6]==ficha1):return 1
    elif(posiciones[0]==ficha1 and posiciones[1]==ficha1 and posiciones[2]==ficha1):return 1
    elif(posiciones[0]==ficha1 and posiciones[4]==ficha1 and posiciones[8]==ficha1):return 1
    elif(posiciones[1]==ficha1 and posiciones[4]==ficha1 and posiciones[7]==ficha1):return 1
    elif(posiciones[2]==ficha1 and posiciones[4]==ficha1 and posiciones[6]==ficha1):return 1
    elif(posiciones[2]==ficha1 and posiciones[5]==ficha1 and posiciones[8]==ficha1):return 1
    elif(posiciones[3]==ficha1 and posiciones[4]==ficha1 and posiciones[5]==ficha1):return 1
    ficha2 = j2['ficha']
    if(posiciones[0]==ficha2 and posiciones[3]==ficha2 and posiciones[6]==ficha2):return 2
    elif(posiciones[0]==ficha2 and posiciones[1]==ficha2 and posiciones[2]==ficha2):return 2
    elif(posiciones[0]==ficha2 and posiciones[4]==ficha2 and posiciones[8]==ficha2):return 2
    elif(posiciones[1]==ficha2 and posiciones[4]==ficha2 and posiciones[7]==ficha2):return 2
    elif(posiciones[2]==ficha2 and posiciones[4]==ficha2 and posiciones[6]==ficha2):return 2
    elif(posiciones[2]==ficha2 and posiciones[5]==ficha2 and posiciones[8]==ficha2):return 2
    elif(posiciones[3]==ficha2 and posiciones[4]==ficha2 and posiciones[5]==ficha2):return 2
    ocupadas = 0
    for i in range(len(posiciones)):
        if(posiciones[i] != i):
            ocupadas += 1
    if(ocupadas == len(posiciones)):
        return 3
    return 0

# Parte 1
def main():
    jugadores = []
    fin = False
    while(fin == False):
        menu()
        opcion = int(input(""))
        if(opcion != 4):
            llamada_funciones(opcion,jugadores)
        else:
            print("**Hasta luego**")
            fin = True
        

main()