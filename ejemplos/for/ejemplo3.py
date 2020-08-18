palabra = input("Ingrese una palabra: ")
nueva_palabra = ""
for i in palabra:
    if(i.islower()):
        nueva_palabra += i.upper()
    elif(i.isupper()):
        nueva_palabra += i.lower()
print("Palabra nueva: ",nueva_palabra)