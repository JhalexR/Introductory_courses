# Funcion Concat

# En Pandas, dos DataFrames se pueden concatenar usando el método concat(). 

# libreria necesaria para usar Merge
import pandas as pd
 
# comenzaremos creando dos DataFrames de ejemplo. 
# En el primer DataFrame de muestra,tenemos información sobre algunos empleados en una empresa:
# Creando DataFrame 1
df1 = pd.DataFrame({
    'Nombre': ['John', 'Jack', 'Steve', 'Sarah'],
    'Edad': [24, 32, 19, 29],
    'Género': ['M', 'M', 'M', 'F']
})
# DataFrame que se ve así:

#     Nombre    Edad    Género
# 0   John      24      M
# 1   Jack      32      M
# 2   Steve     19      M
# 3   Sarah     29      F


# tenemos otro DataFrame que contiene información sobre los departamentos en la empresa:
# Creando DataFrame 2
df2 = pd.DataFrame({
    'Departamento': ['Marketing', 'Ventas', 'Recursos Humanos'],
    'Empleados': [15, 12, 10],
})
# DataFrame que se ve así:

#     Departamento      Empleados
# 0   Marketing          15
# 1   Ventas             12
# 2   Recursos Humanos   10

# Ahora, podemos usar el método concat() para combinar los dos DataFrames verticalmente:
# Concatenando verticalmente
df3 = pd.concat([df1, df2], axis=0) 

# el parámetro axis=0 denota que queremos concatenar los DataFrames apilándolos uno encima del otro (es decir, verticalmente).
# Después de la concatenación, obtenemos la siguiente salida:

#     Nombre  Edad    Género  Departamento     Empleados
# 0   John    24      M       NaN              NaN
# 1   Jack    32      M       NaN              NaN  
# 2   Steve   19      M       NaN              NaN
# 3   Sarah   29      F       NaN              NaN
# 0   NaN     NaN     NaN     Marketing        15
# 1   NaN     NaN     NaN     Ventas           12
# 2   NaN     NaN     NaN     Recursos Humanos 10

# Concatenando dos DataFrames horizontalmente
# También podemos concatenar dos DataFrames horizontalmente (es decir, combinarlos uno al lado del otro) 
# usando el método concat(), así:
# Concatenando horizontalmente
df4 = pd.concat([df1, df2], axis=1)

# Aquí, el parámetro axis=1 denota que queremos concatenar los DataFrames poniéndolos uno al lado del otro (es decir, horizontalmente). 
# Después de Concatenación, obtenemos la siguiente salida:

#     Name    Age Gender     Department        Employees
# 0   John    24     M        Marketing        15
# 1   Jack    32     M        Sales            12
# 2   Steve   19     M        Human Resources  10
# 3   Sarah   29     F        NaN              NaN