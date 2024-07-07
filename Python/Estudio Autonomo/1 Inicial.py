print("Hola Mundo")

#declarar variables no hay palabras reservadas
nombre = "Alexander" #automaticamente es string
numero = 89          #automaticamente es int
flotante = 3.14      #automaticamente es float

#la funcion type muestra el tipo de dato que es la variable
print(type(nombre))
print(nombre)
print(type(numero))
print(numero)
print(type(flotante))
print(flotante)

num1 = 40       #python la deduce como int
num2 = 99.99    #python la deduce como float

#convertir el tipo de variable

print(int(num2))    #la funcion int dentro de print MUESTRA la parte entera de un float 
print(float(num1))  #la funcion int dentro de print MUESTRA como float a un entero

print(num2)

float(num1)         #la funcion float cuando se usa sola CAMBIA el tipo de variable a float
print(num1)         
print(type(num1))

float(num2)         #la funcion int cuando se usa sola CAMBIA el tipo de variable a int
print(num2)         
print(type(num2))

#operadores aritmeticos

print(4 + 5)    #suma
print(4 - 5)    #resta
print(4 / 5)    #division
print(4 * 5)    #multiplicacion

print(4 ** 5)   #exponenciacion
print(4 // 5)   #division entera
print(4 % 5)   #modulo o residuo

#operadores aritmeticos con uso de variables
num1 = 100
num2 = 50
num3 = 25
num4 = 10

print(num1+num2) #para mostrar el resultado por pantalla
suma = num1+num2 #capturarlo en otra variable

#jerarquia de operadores

print(num1+num2*num3) #primero es la * 

print((num1+num2)*num3) #primero es la + 

print((num1+num2)*num3-num4) #aun primero es la + 

print((num1+num2)*(num3-num4)) #primero es la + luego - y ultimo *

print((num1+num2)*(num3-num4)/(num1-num4)) #primero es la + luego - y ultimo * y /

