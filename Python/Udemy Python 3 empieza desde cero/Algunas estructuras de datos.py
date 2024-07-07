# detalle de algunas estructuras de datos

# En Python, las tuplas, diccionarios, colecciones y arrays son estructuras de datos 
# que tienen diferentes usos y características. 

# A continuación se describen las diferencias entre ellas:

# Tuplas
# Definición: Una tupla es una colección ordenada e inmutable de elementos.
# Sintaxis: Se define utilizando paréntesis () y puede contener elementos de diferentes tipos.
# Inmutabilidad: Una vez creada, no se puede modificar (no se pueden agregar, eliminar o cambiar elementos).
# Uso: Ideal para almacenar un grupo fijo de valores que no deberían cambiar a lo largo del programa.

mi_tupla = (1, "Hola", 3.14)
print(mi_tupla[0])  # Salida: 1

# Diccionarios
# Definición: Un diccionario es una colección desordenada de pares clave-valor.
# Sintaxis: Se define utilizando llaves {} con pares clave
# separados por comas.
# Acceso a elementos: Se accede a los valores mediante las claves, no por índice.
# Mutabilidad: Los diccionarios son mutables, es decir, se pueden agregar, 
# eliminar o modificar pares clave-valor.
# Uso: Útil para almacenar datos donde se necesite un acceso rápido a los valores mediante claves.

mi_diccionario = {"nombre": "Juan", "edad": 30}
print(mi_diccionario["nombre"])  # Salida: Juan

# Listas (Colecciones)
# Definición: Una lista es una colección ordenada de elementos.
# Sintaxis: Se define utilizando corchetes [] y puede contener elementos de diferentes tipos.
# Mutabilidad: Las listas son mutables, es decir, se pueden agregar, eliminar o modificar elementos.
# Uso: Ideal para almacenar secuencias de elementos donde el orden es importante 
# y se puede necesitar modificar el contenido.

mi_lista = [1, "Hola", 3.14]
print(mi_lista[1])  # Salida: Hola
mi_lista.append("nuevo")
print(mi_lista)  # Salida: [1, "Hola", 3.14, "nuevo"]

# Arrays (Módulo array)
# Definición: Un array es una colección ordenada de elementos del mismo tipo.
# Sintaxis: Se define utilizando el módulo array de Python.
# Mutabilidad: Los arrays son mutables, es decir, se pueden agregar, 
# eliminar o modificar elementos.
# Uso: Ideal para almacenar secuencias de elementos del mismo tipo, 
# proporcionando una gestión de memoria más eficiente para grandes 
# colecciones de datos homogéneos.
# Nota: En Python, se suelen usar más comúnmente las listas y el módulo numpy 
# para trabajo con arrays debido a su mayor flexibilidad y funcionalidad

import array as arr

mi_array = arr.array('i', [1, 2, 3, 4])
print(mi_array[2])  # Salida: 3
mi_array.append(5)
print(mi_array)  # Salida: array('i', [1, 2, 3, 4, 5])

# Diferencias Clave

# Mutabilidad: Las tuplas son inmutables, mientras que las listas, diccionarios y arrays son mutables.

# Orden: Las tuplas y listas mantienen el orden de los elementos, 
# mientras que los diccionarios, en versiones modernas de Python (a partir de Python 3.7), 
# también mantienen el orden de inserción. Los arrays son ordenados.

# Acceso: En listas y tuplas, el acceso a los elementos se hace por índice. 
# En diccionarios, el acceso es por clave. En arrays, el acceso es por índice.

#Tipo de elementos: Los arrays requieren que todos los elementos sean del mismo tipo, 
# mientras que listas, tuplas y diccionarios pueden contener elementos de diferentes tipos

# Ejemplo Comparativo

# Tupla
mi_tupla = (1, "Hola", 3.14)
# Diccionario
mi_diccionario = {"nombre": "Juan", "edad": 30}
# Lista
mi_lista = [1, "Hola", 3.14]
# Array
import array as arr
mi_array = arr.array('i', [1, 2, 3, 4])

print("Tupla:", mi_tupla)
print("Diccionario:", mi_diccionario)
print("Lista:", mi_lista)
print("Array:", mi_array)