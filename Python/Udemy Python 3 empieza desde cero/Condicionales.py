edad = int(input("introduce tu edad: "))

# no llevan { } pero si llevan ":" cuando la condicion
# es un numero
# es muy importante la identacion sin ella
# el interprete no reconoce que va dentro dekl bloque 
# de codigo bien sea un if, un ciclo, un metodo lo reconocera
# como parte de ese bloque si esta correctamente tabulado
if edad >= 18 :
    print("eres mayor de edad")
else :
    print("eres menor de edad")

# sentencia if not

# supongamos que no se requiera ningun mensaje de
# salida para el numero 16

# primera opcion
if edad != 16 : # en caso de escribir 16 terminara el programa sin ningun mensaje
    print(f"tienes", edad, "años de edad")

# opcion con if not
if not edad == 16 : # en caso de escribir 16 terminara el programa sin ningun mensaje
    print(f"tienes", edad, "años de edad")