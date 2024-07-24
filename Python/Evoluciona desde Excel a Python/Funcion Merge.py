# Funcion Merge

# libreria necesaria para usar Merge
import pandas as pd

df1 = pd.DataFrame({
    "Mes": ["ene", "feb", "mar", "may"],
    "Ventas": [14, 8, 12, 17]
})
df1

# la base de datos seria:
# indice    Mes     Ventas
# 0         ene     14
# 1         feb     8
# 2         mar     12
# 3         may     17

df2 = pd.DataFrame({
    "Mes": ["feb", "ene", "mar", "abr"],
    "Costo": [7, 6, 8, 5]
})
df2

# la base de datos seria:
# indice    Mes     Costos
# 0         feb     7
# 1         ene     6
# 2         mar     8
# 3         abr     5

# Vemos que ambos dataframes tienen una columna común ("Month") y varias filas comunes ("ene", "feb" y "mar").
# Obsérvese que en df2 las filas no están ordenadas y que, en df1, el mes de enero tiene índice 0 
# mientras que, en df2, el mes de enero tiene índice 1.

# Si aplicamos la función merge a estos dataframes con los valores por defecto, 
df_merge = pd.merge(df1,df2)
print(df_merge)

# obtenemos el siguiente resultado:
# indice    Mes     Ventas  Costos
# 0         ene     14       6
# 1         feb     8        7
# 2         mar     12       8

# Esos valores por defecto suponen que el join se realiza sobre las columnas comunes 
# y tipo "inner" (considerando solo las filas con etiquetas comunes).

# Si especificamos que el join sea de tipo "outer", lo que definimos con el parámetro how, 
# el resultado considerará todas las etiquetas presentes en ambos dataframes:

df_merge = pd.merge(df1,df2, how="outer")
print(df_merge)

# obtenemos el siguiente resultado:
# indice    Mes     Ventas  Costos
# 0         ene     14       6
# 1         feb     8        7
# 2         mar     12       8
# 3         may     17       N/A
# 4         abr     N/A      5

# Como vemos, se ha rellenado con NaN's los valores inexistentes. 

# si usamos en how el valor "left" se tomara como base la primera base de datos
print("left")
df_merge = pd.merge(df1,df2, how="left")
print(df_merge)
# obtenemos el siguiente resultado:
#    Mes  Ventas  Costo
# 0  ene      14    6.0
# 1  feb       8    7.0
# 2  mar      12    8.0
# 3  may      17    NaN

# si usamos en how el valor "left" se tomara como base la segunda base de datos
print("rigth")
df_merge = pd.merge(df1,df2, how="right")
print(df_merge)
# obtenemos el siguiente resultado:
#    Mes  Ventas  Costo
# 0  feb     8.0      7
# 1  ene    14.0      6
# 2  mar    12.0      8
# 3  abr     NaN      5

# También podría ocurrir que ambos dataframes no tuviesen columnas comunes (columnas con el mismo nombre) 
# pero que, aun así, quisiéramos realizar el join por algunas de ellas. Por ejemplo:

df1 = pd.DataFrame({
    "Mes": ["ene", "feb", "mar", "may"],
    "Ventas": [14, 8, 12, 17]
})
df1

df2 = pd.DataFrame({
    "Month": ["feb", "ene", "mar", "abr"],
    "Costo": [7, 6, 8, 5]
})
df2

# Al no haber columnas comunes, la ejecución de la función merge devolvería un error. 
# En este caso podemos usar los parámetros left_on y right_on para especificar 
# el campo a usar en la tabla de la izquierda del join y en la de la derecha, respectivamente:

df_merge = pd.merge(df1,df2, left_on="Mes", right_on="Month")
print(df_merge)

# indice    Mes     Ventas  Month   Costo
# 0         ene     14      ene     6
# 1         feb     8       feb     7
# 2         mar     12      mar     8