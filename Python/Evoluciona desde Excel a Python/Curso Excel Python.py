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
print(fifa.head())

# funcion muestra el nombre de las columnas de la base de datos
print(fifa.columns.values)

# funcion muestra el nombre de las columnas de la base de datos en en una fila
print(fifa.columns.values.tolist)

# funcion muestra la cantidad de filas y columnas de la base de datos en en una fila
print(fifa.shape)

# funcion muestra las principales medidas estadisitcas de las columnas numericas
print(fifa.describe())

# funcion muestra informacion importante de la base como datos nullos y tipo de datos
print(fifa.info())

