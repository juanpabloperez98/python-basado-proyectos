while(True):
    nombre = input("Ingrese nombre de login: ")
    longitud = len(nombre)
    if(longitud < 4): print("**Longitud menor a 4**")
    elif(longitud > 15): print("**Longitud mayor a 15**")
    else: break
print("El nombre de usuario es: {}".format(nombre))