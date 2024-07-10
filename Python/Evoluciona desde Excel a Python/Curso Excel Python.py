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
fifa_final.to_excel("Base_final.xlsx", index=False) # sin columna index