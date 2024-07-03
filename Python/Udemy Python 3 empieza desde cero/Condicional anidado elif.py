# la sentencia If-Elif-Else

# Las sentencias IF e If-else solo son útiles para situaciones binarias.

# En el caso de un problema condicional múltiple, se utiliza la sentencia 
# «if-elif-else».

# En primer lugar, se comprueba la condición de la sentencia If. 
# Si es falsa, se evalúa la sentencia Elif. 
# Si la condición también es falsa, se evalúa la sentencia Else.

# En Python, la sentencia «Elif» se utiliza para comprobar múltiples
# condiciones si una condición es falsa. 
# Es similar a la sentencia «If-Else», 
# pero la diferencia es que «Elif» 
# evalúa múltiples condiciones a diferencia de «Else».  
  
edad = int(input("introduce tu edad: "))
mes = int(input("introduce tu mes de nacimiento: "))

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
