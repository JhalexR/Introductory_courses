#La función range() en Python se utiliza para generar una secuencia de números. 
 
# Es especialmente útil en bucles for, donde se necesita iterar un número específico de veces
# o a través de una serie de números.

# Sintaxix range
# range(stop)
# range(start, stop[, step])

# Parámetros
# stop: El límite superior de la secuencia. La secuencia generada no incluye este valor.
# start (opcional): El valor inicial de la secuencia. El valor predeterminado es 0.
# step (opcional): La diferencia entre cada par de números consecutivos en la secuencia. El valor predeterminado es 1.

# Ejemplos

# 1. Usando un solo argumento (stop)
for i in range(5):
    print(i)
# Genera una secuencia de números desde 0 hasta 
# (pero sin incluir) el número especificado.
print('otra')

# 2. Usando dos argumentos (start, stop)
for i in range(2, 7):
    print(i)
# Genera una secuencia de números desde el valor inicial 
# hasta (pero sin incluir) el valor final.
print('otra')

# 3. Usando tres argumentos (start, stop, step)
for i in range(1, 10, 2):
    print(i)
# Genera una secuencia de números 
# desde el valor inicial hasta (pero sin incluir) el valor final, 
# incrementando o disminuyendo por el valor de step.
print('otra')

# 4. Usando un step negativo
for i in range(10, 0, -2):
    print(i)
# Genera una secuencia decreciente de números.
print('otra')

# Usos Comunes

# Iterar un número específico de veces:
for _ in range(5):
    print("Hello")

# Generar índices para listas:
my_list = ['a', 'b', 'c', 'd']
for i in range(len(my_list)):
    print(f"Index {i} contains {my_list[i]}")

# Generar secuencias numéricas:
numbers = list(range(1, 11))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]