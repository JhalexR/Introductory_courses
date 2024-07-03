#conceptos basicos iniciales

print("Hola mundo")

#las variables no se declaran, solo se coloca el nombre
name = "nombre"
print(name)

#con asignarles un valor diferente cambian de tipo

name = 55

name = 55-1

print(name)

#variables de tipo numerico

num_1 = 20
num_2 = 5

print(num_1)
print(num_2)

#no existen declaraciones de tipo de variable numerica

num_2 = num_2/num_1
print(num_2) 

#imprime decimal sin necesidad de declararlo

#cadenas de caracteres

cadena_1 = "primer"
cadena_2 = "ejemplo"

#formas de impresion

#forma 1

print(cadena_1, cadena_2)

#forma 2

print("este es:", cadena_1, cadena_2)

#forma 3

print(f'este es: {cadena_1} {cadena_2}')

#imprimir resultados de operaciones

print(f'tengo {10+10} años')

#imprimir varias veces la misma variable

print(cadena_1*5)

#Vectores

vector_1 = ["Python", "Django", "React", "Vue"]

print(vector_1[0])

#cuando se usa numero negativos 
#empieza por el final
print(vector_1[-1])

#modificar en el vector
vector_1[1] = "Flutter"

#añadir un dato al final del vector
vector_1.append("Angular")
print(vector_1[4])

#añadir un dato en posicion especifica del vector
vector_1.insert(1,"Angular")
print(vector_1[1])

#Tuplas
#diferencia con vector, 
#sus datos no se pueden modificar

#en vectores se usa [] en tuplas()
tupla_1 = ("python", "Django", "React", "Vue")
print(tupla_1[1])

#Diccionarios
#diccionario son datos relacionados 
data ={"name":"Ceraspio,", "last_name": "Joso", "edad": "18"}

#nos permite imprimir datos llamando al nombre
#indice o nombre de variable
#imprimir un dato del diccionario
print(data["last_name"])#imprime "Joso"

#imprimir con concatenacion
print(f"mi apellido es {data["last_name"]}")#imprime "Joso"

#añadir datos al diccionario
data["city"] = "Veraguas"
print(data["city"])

#eliminar un dato de diccionario
del data["edad"]#elimina la clave "edad" del diccionario

#saber cuantas claves hay en el diccionario
print(len(data))

#recibir datos por consola
name = input("introduce tu nombre: ")
last_name = input("introduce tu apellido: ")
edad = input("introduce tu edad: ")

print(f"Me llamo {name} {last_name} y tengo {edad} años")

#operar numeros ingresados por consola
num_1 = input("primer numero: ")
num_2 = input("segundo numero: ")

#para poder operar los numeros introducidos 
#se tiene que modificar el tipo de variable 
#ya que la funcion input los almacena como string
print(int(num_1)+int(num_2))

#control de datos 
#se puede cambiar el tipo de dato desde el input
num_1 =int(input("primer numero: "))
num_2 = int(input("segundo numero: "))

print(num_1 + num_2)

#ejemplo tipos de datos a los que se puede cambiar
#float, int, bool, str

#se modifica de int a bool
num_1 =int(input("primer numero: "))
print(bool(num_1)) #imprimira True si es >= 1