edad = int(input("introduce tu edad: "))
mes = int(input("introduce tu mes de nacimiento: "))

# En Python, la sentencia «Elif» se utiliza para comprobar múltiples
# condiciones si una condición es falsa. 
# Es similar a la sentencia «If-Else», 
# pero la diferencia es que «Elif» 
# evalúa múltiples condiciones a diferencia de «Else».    


if edad >= 18:
    print("Eres mayor de edad")
    if mes == 1:
        print("Naciste en enero")
    elif mes == 2: # sentencia elif
        print("Naciste en febrero")
else:
    print("Eres menor de edad")
    if(mes==3):
        print("Naciste en marzo")
