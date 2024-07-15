# Curso Excel Python

# importando librerias importante instalarlas anteriormente
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargando base de datos

# 1 metodo de carga base de datos desde archivo .CSV
fifa = pd.read_csv(r"C:\Users\JohnAlexanderPeñaloz\OneDrive - PayU\Principal\2024\Git\Introductory_courses\Python\Evoluciona desde Excel a Python\data.csv", sep=",")

# 2 metodo de carga base de datos desde archivo .xlsx
fifa_2 = pd.read_excel(r"C:\Users\JohnAlexanderPeñaloz\OneDrive - PayU\Principal\2024\Git\Introductory_courses\Python\Evoluciona desde Excel a Python\data.xlsx")

# 2 metodo de carga base de datos desde SQL
# import pyodbc 
# server = "xxx.xxx.xxx..."
# database = "nombre_base"
# username ="username"
# password = "password"
# driver = "SQL_server"
# port = xxx
# cnn = pyodbc.connect('DRIVER='+driver+';PORT=port;SERVER='+server+';PORT=port;DATABASE='+database+';UID='+username+';PWD='+password+')
# cursor = cnn.cursor()

# fifa_3 = pd.read_sql("SELECT * FROM Nombre_Tabla", cnn)

# revision de la base de datos

# funcion head muestra las 5 primeras filas de la base de datos con todas las columnas
fifa.head()

# funcion muestra el nombre de las columnas de la base de datos
fifa.columns.values

# funcion muestra el nombre de las columnas de la base de datos en en una fila
fifa.columns.values.tolist

# funcion muestra la cantidad de filas y columnas de la base de datos en en una fila
fifa.shape

# funcion muestra las principales medidas estadisitcas de las columnas numericas
fifa.describe()

# funcion muestra informacion importante de la base como datos nullos y tipo de datos
fifa.info()

# filtrar bases de datos

# filtro por nombre de columnas
fifa_filtro_1 = fifa[["ID","Name","Age"]]

# filtro por funcion drop - eliminar columnas o filas
fifa_elim_column = fifa.drop("Unnamed: 0", axis=1) # eliminar comlumna axis = 1, eliminar fila axis = 0
fifa_elim_columns = fifa.drop(["Unnamed: 0", "ID"], axis=1) # eliminar varias comlumnas [ ]
# para eliminar filas se coloca el numero de la fila
fifa_elim_fila = fifa.drop(0, axis=0) # elimina la fila en la posicion 0

# filtro por loc e iloc

# filtro por loc
fifa_loc = fifa.loc[:,["Name", "Age"]]# para filtrar por loc es por nombre de la columna

# filtro por iloc
fifa_iloc = fifa.iloc[0:10] # filtra las primeras 10 filas
fifa_iloc = fifa.iloc[10] # filtra solo la fila 10
fifa_iloc = fifa.iloc[0:10,0:10] # filtra las primeras 10 filas y las primeras 10 columnas
fifa_iloc = fifa.iloc[:,0:10] # para filtra solo las primeras 10 columnas pero no filtrar ninguna fila
fifa_iloc = fifa.iloc[0:10,:] # para filtra solo las primeras 10 filas pero no filtrar ninguna columna
fifa_iloc = fifa.iloc[:,[2,5,9]] # para filtra por columnas

# Filtrando base de dtos con la que se va a trabajar con iloc
fifa_final = fifa.iloc[:,1:28] # se filtran las primeras 28 columnas que son las que se van a usar

# filtro por valores especificos - similar a Excel -
Fifa_barcelona = fifa[fifa["Club"]=="FC Barcelona"] # filtrando por el valor Club Barcelona 
Fifa_dif_barcelona = fifa[fifa["Club"]!="FC Barcelona"] # filtrando por el valor diferentes al Club Barcelona
Fifa_menor_30 = fifa[fifa["Age"]<30] # filtrando por jugadores menores de 30 años

# filtro compuesto mas de dos categorias
fifa_mas_30_Brasil = fifa[(fifa["Age"]>30)&(fifa)["Nationality"]=="Brazil"] # filtro de jugadores mayores a 30 años y de Brasil
fifa_mas_30_Brasil = fifa[(fifa["Age"]>30)|(fifa)["Nationality"]=="Brazil"] # filtro de jugadores mayores a 30 años o de Brasil

#filtro por valores de texto que contengan parte de una palabra 
fifa_parte_nombre = fifa[fifa["Name"].str.contains("Sergio")] # filtrar elementos que en la columna "Name" contengan la parte "Sergio"

# filtro funcion .isin filtra por los criterios de una lista
lista = ["Brazil", "Chile", "Argentina"]
fifa_lista = fifa[fifa["Nationality"].isin(lista)]

# Exportar a excel

# Exportar a .CSV
fifa_final.to_csv("Base_final.csv")

# Exportar a .xlsx
fifa_final.to_excel("Base_final.xlsx", index=False) # sin la columna index

# Campos vacios o nulos

# eliminando columna especifica que consideremos tiene muchos datos nulos
fifa_final = fifa_final.dropna("Loaned From", axis=1) # para eliminar una columna especifica se coloca el nombre de la columna

# Eliminando columnas que tengan datos nulos
fifa_final = fifa_final.dropna(axis=1) # elimina todas las columnas que tengan algun dato que sea nulo

# Eliminando filas que tengan datos nulos
fifa_final = fifa_final.dropna(axis=0) # en este caso elimia todas las filas que tengan algun dato nulo

fifa_final = fifa_final.dropna(how="any",axis=0) # elimina filas que tengan cualquier dato nulo

fifa_final = fifa_final.dropna(how="any",axis=0) # elimina filas que todos sus datos sean nulos

# reemplazar valores nulos

fifa_final = fifa_final.fillna(0) # reemplaza todas las celdas vacias por "0"

fifa_final = fifa_final.fillna("valor nulo") # reemplaza todas las celdas vacias por "valor nulo"

fifa_final["Club"] = fifa_final["Club"].fillna("sin club") # reemplazar los valores nulos de una columna especifica

# funcion Value Counts -recuento-

# funcion Value counts -recuento- se aplica sobre datos que sean strings o variables categoricas generalmente no numerica
fifa_final = ["Nationality"].value_counts(sort=False) # -recuento- cuenta los registros de esa columna ordenada de menor a mayor
fifa_final.Nationality.value_counts(sort=False) # -recuento- cuenta los registros de esa columna ordenada de menor a mayor igual segunda forma

# mostrar top 10 -recuento-
fifa_final.Nationality.value_counts().nlargest(10) # -recuento- muestra el top 10 de registros con mayor valor de esa columna
fifa_final.Nationality.value_counts().nsmallest(10) # -recuento- muestra el top 10 de registros con menor valor de esa columna

# mostrar contar -recuento- con calculo %
fifa_final.Nationality.value_counts(normalize=True).nsmallest(10) # muestra el top 10 por %

# funcion Value Counts -recuento- variables numericas
# hacer intervalos
fifa_final.Nationality.value_counts(bins=5) # intervalos con datos numericos
fifa_final.Nationality.value_counts(bins=5, normalize=True) # intervalos con porcentajes

# Cambiar el formato de los datos
# funcion astype
fifa_final = fifa_final.ID.astype(str) # cambiar el ID que estaba en int a string

# cuando el nombre de una columna o variable tiene espacios en blanco no usar sentencia con puntos es necesario usar []
fifa_final["International Reputation"] = fifa_final["International Reputation"].astype(int) # cambiar de float a int 

# agregar nuevas columnas
# crear una nueva columna que se va rellenar automaticamente con el numero 1 en todas sus celdas
fifa_final["Cuenta"] = 1 # el nombre de la nueva columna en este caso es "Cuenta"

# crear columna de clave que es la union de datos que haya en la fila para hacer identificadores
fifa_final["Clave"] = fifa_final["Nationality"] + "-" + fifa_final["Name"] # concatenar columnas se hace con el "+"

# para unir variables en una nueva columna deben ser del mismo tipo de datos 
# si no son del mismo se debe realizar conversion solo para la nueva columna y no para las columnas originales
fifa_final["Clave"] = fifa_final["Nationality"] + "-" + fifa_final["Age"].astype(str) # convierte los datos a string en la nueva columna

# Funcion Where -> (numpy)
# la funcion where cumple la funcion condicional "cuando"
# en este caso se va a crear una columna donde colocaremos el rango de carrera del jugador
fifa_final["Proximo_retiro"]  = "Apprentice" # se crea la columna "Proximo_retiro" y se rellena por defecto con "Apprentice" como si todos los jugadores acabaran de iniciar

# en esta sentencia la funcion where pregunta si en la fila en la columna "Age" es >=34 y de ser asi cambia el contenido a "Veteran"
fifa_final["Proximo_retiro"]  = np.where(fifa_final["Age"]>=34, "Veteran", fifa_final["Proximo_retiro"])

# en esta sentencia la funcion where pregunta si en la columna "Age" es <34 y >30 de ser asi cambia el contenido a "Experienced"
fifa_final["Proximo_retiro"]  = np.where(fifa_final["Age"]<34 & fifa_final["Age"]>=30, "Experienced", fifa_final["Proximo_retiro"])

# en esta sentencia la funcion where pregunta si en la columna "Age" es <30 y >=25 de ser asi cambia el contenido a "Rookie"
fifa_final["Proximo_retiro"]  = np.where(fifa_final["Age"]<30 & fifa_final["Age"]>=25, "Rookie", fifa_final["Proximo_retiro"])

# al terminar el bloque de sentencias "where" la comlumna "Proximo_retiro" tendra cada fila 
# con la informacion actualizada de rango de carrera de cada jugador de acuerdo a su edad

