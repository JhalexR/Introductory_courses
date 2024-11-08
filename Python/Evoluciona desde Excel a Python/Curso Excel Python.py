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

# Crear funciones 
# las funciones creadas se pueden usar varias veces en diferentes momentos del codigo
# Creacion y definicion de funcion prueba
def prueba(x):
    return  x * 2 # funcion tiene como argumento un valor y lo multiplica 2

# Se crea una nueva columna que va a contener el resultado de aplicar la funcion a una columna
fifa_final["Cuenta * 2"] = fifa_final["Cuenta"].apply(prueba) # a la columna "Cuenta" se le aplica la funcion "prueba" y se alamcenaran resultados en "Cuenta * 2"

# creacion y definicion de funcion "Proximo_retiro"
# se crea una funcion para establecer el tiempo o rango de carrera del jugador como s ehizo en un ejemplo anterior
# pero usando funcion
def func_proximo_retiro(x):
    if x >=34:
        return "Veteran"
    elif x >=30:
        return "Experienced"
    elif x >=25:
        return "Rookie"
    return "Apprentice"

# uso funcion creada llamada "func_proximo_retiro"
fifa_final["Proximo_retiro"] = fifa_final["Age"].apply(func_proximo_retiro) # se aplica la funcion a la columna "Age" y se alamcena en "Proximo_retiro"

# realizar la misma tarea que la funcion anterior "prueba" pero con for
fifa_final["Cuenta * 2"] = [x * 2 for x in fifa_final["Cuenta"]] # recorre con for la columna "cuenta" y aplica x*2 mientras aumenta for y alamacena en nueva columna "Cuenta * 2" 

# funcion si o if de excel en python
# reocorre la columna "Proximo_retiro" si el contenido diferente de "Veteran" coloca si en la nueva columna "Opcion de compra"] en caso contrario coloca "No"
fifa_final["Opcion de compra"] = ["Si" if x!="Veteran" else "No" for x in fifa_final["Proximo_retiro"]] 

# funcion Merge reemplazo de buscarV y tiene mas opciones
# primer paro creamos una base de datos con las columnas que vamos a usar 
# la base original tiene 18207 filas pero el maximo de filas con datos en las columnas seleccionadas es de 17549
fifa_filtro_1 = fifa_final[0:17549,[1,77,79,88]] # la nueva base contiene las columnas 1, 77, 79 y 88 con las que se hara la busqueda
# uso de la funcion Merge
fifa_Merge = [pd.merge(left=fifa_final, right=fifa_filtro_1, how='left', on="ID")] 
# una mejor explicacion de la funcion Merge en reemplazo de la funcion buscarV en archivo de esta misma carpeta llamado Merge

# funcion lookup es similar a buscarH en excel

# primero creamos una lista con algunos de los paises que estan e la columna Nationality de la base que estamos manejando
lista = {"Brazil", "Argentina", "Chile", "Francia"}
# creamos nueva base de datos solo con los datos de la columna "Nationality" que se encuentren en la "lista"
fifa_paises = fifa_final(fifa_final["Nationality"].isin(lista)) # con la funcion "isin" llenamos la nueva base solo con los paises de la "lista"  
# esta funcion esta deprecated y se usa en su lugar la funcion .melt combnada con .loc

# la funcion Concat en python une dos bases de datos coloca al final de una base de datos la segunda base de datos
# util para cuando se esta consolidando informacion de bases de datos que se van actualizando con el tiempo
fifa_parte_1 = fifa_final.iloc[0:60] # base de datos de las primeras 60 filas de la base de datos total 
fifa_parte_2 = fifa_final.iloc[120:180] # base de datos de las filas desde la 120 a la 180 de la base de datos total
# se usa la funcion concat para unirlas en una sola base de datos por filas es decir primero una base y en cuando termine en la siguiente fila la otra base
fifa_parte_1_and_parte_2 = pd.concat([fifa_parte_1,fifa_parte_2], axis=0) # axis=0 indica que se uniran las bases por filas
# en caso de que las bases de datos tengan columnas en comun pero no la misma cantidad de columnas
# la funcion concat localiza donde se encuentra la misma columna en la primer base de datos y anexa la informacion de la misma columna 
# en la segunda base de datos, evitando que se crucen columnas, las columnas de la primera base de datos le seran anexadas
# los datos de la segunda base de datos coincidiendo en las mismas columnas, en las columnas que solo esten en la primera 
# base de datos quedaron valores vacios o nulos en las nuevas filas anexadas de la segunda base de datos

# eliminar duplicados

fifa_parte_1.id.nunique() # la funcion nunique muestar si hay datos duplicados en alguna columna
fifa_parte_1 =  fifa_parte_1.drop_duplicates() # la funcion .drop_duplicates elimina duplicados donde las filas sean en todos sus campos o columnas iguales
# con El parametro "subset" la columna guia para quitar duplicados y el parametro "keep" es para dejar conservar la primera fila que encuentre y borrar las demas
fifa_parte_1 =  fifa_parte_1.drop_duplicates(subset="Nationality", keep='first') 
# para eliminar por mas de una columna de guia
fifa_parte_1 =  fifa_parte_1.drop_duplicates(subset=["Position", "Age"], keep='last') # conserva la ultima fila que encuentre

# ordenar valores
# ordenar de menor a mayor 
fifa_final = fifa_final.sort_values("Age") # por defecto ordena de menor a mayor 
# ordenar de mayor a menor  
fifa_final = fifa_final.sort_values("Age",ascending=False) # para ordenar de mayor a menor
# en este caso asume que "Age" es numerica y "Nationality" es alafabetica  
fifa_final = fifa_final.sort_values(["Age","Nationality"],ascending=True)

# argumento inplace
# argumento in place sirve para actualziar la base de datos que se esta unsado sin necesidad de generar una variable
# o realizar la asignacion en la variable
# forma normal:
fifa_final = fifa_final.sort_values(["Age","Nationality"],ascending=True)
# forma con inplace
fifa_final.sort_values(["Age","Nationality"],ascending=True, inplace=True) # no se usa , "fifa_final =" o una nueva variable

# operadores logicos
# eq = igualdad
# me = diferente
# le = menor o igual
# lt = menor que
# ge = mayor o igual que
# gt = mayor que
fifa_final["Columna_1"] = fifa_final["Skill Moves"].le(fifa_final["Weak_Foot"]) # en la nueva columna guarda el resultado de "le" entre las dos columnas
fifa_final["Columna_1"] = [1 if x == True else 0 for x in fifa_final["Columna_1"]] # coloca 1 o 0 si es verdadero o falso segun la condicion
# comparar con un valor constante
n = 80
fifa_final["Columna_1"] = fifa_final["Potential"].gt(n) # comprara la columna "Potential" si es mayor o igual a "n"

# Intervalos manuales
# funcion Cut
fifa_final["Intervalos_manuales"] = pd.cut(fifa_final("Jersey Number"), bins=[0,5,15,25,110])
# Agurpa de la columna "Jersey Number" los numeros de camsieta que se encuentren en el rango de los grupos:
#  primer grupo 0 hasta 5
#  segundo grupo 6 hasta 15
#  segundo grupo 16 hasta 25
#  segundo grupo 26 hasta 100
# los guarda en la nueva columna "Intervalos_manuales"
# para incluir el numero menor en cada intervalos usamos el argumento "include_lowest"
fifa_final["Intervalos_manuales"] = pd.cut(fifa_final("Jersey Number"), bins=[0,5,15,25,110], include_lowest=True)

# funciones de texto
# convertir letras de celda en minuscula
fifa_final["Nacion"] = fifa_final["Nationality"].str.lower()
# convertir letras de celda en mayuscula
fifa_final["Nacion"] = fifa_final["Nationality"].str.upper()
# primera letra em mayuscula y las demas en minuscula
fifa_final["Nacion"] = fifa_final["Nationality"].str.capitalize()
# reemplazar texto
fifa_final["Nacion"] = fifa_final["Nationality"].str.replace("a","o") # reemplazar letras "a" por "o"

# funcion Group By

# en Python funciona en tres pasos
# primero se puede separar por algunas de las variables/columnas en grupos
# segundo aplicar una operación como sumar contar promedio etc a estos datos
# tercero combinar los datos

# Primer paso
Grupo = fifa_final.groupby("Nationality") # con esta intruccion guarda en la variable un grupo por cada dato que exista con la variable/columna
# se puede visualizar alguno de los grupos por ejemplo nacionalidad = "Chile"
tabla_Chile = Grupo.get_group("Chile") # guardar la tabla con los datos que en la columna "Nationality" tengan "Chile" 
# se puede mostrar cualquier nacionalidad 

# mostrar promedio "mean()"
promedio = fifa_final.groupby("Nationality")["Age"].mean() # muestra el promedio de edad para cada pais
# con dos argumentos tabla con dos niveles
# agrupa primero por nacionalidad en cada nacionalidad agrupa por club y despues el promedio de dedad por cada club
promedio = fifa_final.groupby(["Nationality", "club"])["Age"].mean() 

# se puede hacer tablas con varias agrupaciones sin usar "get_group" para guardar todo en un solo paso
Chile_edad = fifa_final[fifa_final["Nationality"]=="Chile"].groupby("Proximo_retiro","club")["Age"].mean()
# se agrupo primero los datos que en la columna "Nationality" = "Chile", despues se agrupo por "Proximo_retiro" y "Club" 
# y se saco el promedio de edad por "club" y s eguardo en la variable.

# hacer mas de un calculo de una columna
# en este caso de los datos de "Naitonality" = "Chile" se agrupan los valores que tiene "Proximo_retiro"
# y con los datos de "Age" se calcula el promedio (np.mean) y la desviacion estandar (np.std)
Chile_edad = tabla_Chile.groupby(["Proximo_retiro"])["Age"].agg(np.mean, np.std)

# aplicar funcion colocando mas de una columna en valores aplicando funciones o calculos diferentes
Chile_edad = tabla_Chile.groupby(["Proximo_retiro"]).agg({'Age':np.mean, 'weak_foot':np.sum})
# crea la tabla con los datos de "Naitonality" = "Chile" guardados en la variable "tabla_Chile" 
# la primera fila es "Proximo_retiro" crea dos columnas una con el promedio de "Age" y otra con la suma de weak_foot

# Pivot_table 
# funcion para creacion de tablas dinamicas similar a funcion GroupBY 
# pero se parece mas a las opciones de pivto table de Excel
Tabla_dinamica = pd.pivot_table(fifa_final, index="Nationality", values="Age", aggfunc="mean")
# index = rows, values = valores en Excel, "aggfunc" -> para agregar funcion con los datos, "mean" = promedio, 

# tabla dinamica con funcione "fill_value=0" -> para rellenar espacios en blanco con 0, funciones "margin" para crear totales y el nombre del total
Tabla_dinamica_club = pd.pivot_table(fifa_final, index="club", values="Jersey Number", aggfunc="std", fill_value=0, margins=True, margins_name="Total")

# agregar columnas con la funcion "columns"
Tabla_dinamica_body = pd.pivot_table(fifa_final[(fifa_final["Body type"]!="sin datos") & (fifa_final["Real face"]!="sin datos")], index="body_type", columns="real face", values="Jersey Number", aggfunc="std", fill_value=0, margins=True, margins_name="Total")
# se filtra la base de datos quitando las filas en las que las variables "body_type" y "real face" no tienen datos se coloca como indice o rows los datos de la columna "Body type" se agrega la columna "Real face" y la columna "Jersey numbres" se le calcula desviacnon estandar

# agregar dos calculos a la misma columna en este caso promedio y desviacion estandar
Tabla_dinamica_body = pd.pivot_table(fifa_final[(fifa_final["Body type"]!="sin datos") & (fifa_final["Real face"]!="sin datos")], index="body_type", columns="real face", values="Jersey Number", aggfunc=["mean", "std"], fill_value=0, margins=True, margins_name="Total")
# en este caso al colocar aggfunc=["mean", "std"] los dos calculos que queremos hacer, aparecera las columnas divididas primero por promedio del "Jersey Number" dividido en los datos de la columna "real face" 
# lo mismo con la desviacion estandar de "Jersey Number" tambien divididos por los datos de la columna "real face"

# agregar el mismo calculo a dos variables en este caso "Jersey Number" y "Age" promedio
Tabla_dinamica_body = pd.pivot_table(fifa_final[(fifa_final["Body type"]!="sin datos") & (fifa_final["Real face"]!="sin datos")], index="body_type", values="Jersey Number", aggfunc=({"Jersey Number":"mean", "Age":"std"}),fill_value=0)
# en este caso no es necesario usar "columns" automaticamente se creara una columna con el promedio de "Jersey Number" y otra con el promedio de "Age"

# agregar otro nivel al index u otra row o fila a la tabla solamente debemos agregarla index=["body_type", "Real face"]
Tabla_dinamica_body = pd.pivot_table(fifa_final[(fifa_final["Body type"]!="sin datos") & (fifa_final["Real face"]!="sin datos")], index=["body_type", "Real face"], values="Jersey Number", aggfunc=({"Jersey Number":"mean", "Age":"std"}),fill_value=0)
# de esta forma tendremos dos agrupamientos en las filas

# agregar mas de una columna sin la funcion "columns" y con la funcion "aggfunc"
posicion = pd.pivot_table(fifa_final, index="position", aggfunc=({"cuenta":"sum", "Age":"mean"}))
# En la columna "cuenta" se calcula la suma y en la columna "Age" el promedio de edad

# renombrar columnas 
posicion.columns = ["Position","Edad", "Futbolistas"]
# los anteriores nombres cuenta y Age son reemplazados

# nueva columna similar a campo calculado
posicion["Ratio"] = posicion["Futbolistas"]/posicion["Edad"]
# la nueva columna es la ratio entre el futbolistas / edad

# dar formato con la funcion Style
posicion.style.format({"Edad":"{0:,.1f}", "Futbolistas":"{0:,.0f}", "Ratio":"{:.2%}"})
# esto le dara un decimal a "Edad", "Futbolistas" sin decimales y con separacion de miles y ratio en % con dos decimales 
posicion.style.format({"Edad":"{0:,.1f}", "Futbolistas":"${0:,.0f}", "Ratio":"{:.2%}"})
# en este ejmplo "Futbolistas" pasaria formato moneda

# Style formato condicional
posicion_format = posicion.copy() # copiar tabla en otra variable
posicion.style.format({"Edad":"{0:,.1f}", "Futbolistas":"${0:,.0f}", "Ratio":"{:.2%}"}).background_gradient_color(cmap = "Greens") 
# "Greeens_r" es para invertir el mapa de calor
# la funcion background_gradient_color da el color a la tabla con el color maps cmap degradado como un mapa de calor
# (cmap = "spring") es para diferentes colores vivos 

posicion.style.format({"Edad":"{0:,.1f}", "Futbolistas":"${0:,.0f}", "Ratio":"{:.2%}"}).highlight_max(color="green")
# para agregar color solamente al valor mas alto de la columna
# highlight_min(color="green") es para agregar color solo al valor mas bajo de la comlumna

# para barras de datos de colores
posicion.style.format({"Edad":"{0:,.1f}", "Futbolistas":"${0:,.0f}", "Ratio":"{:.2%}"}).bar(color="Steelblue")

# funcion subset para solo para aplicar el formato de color a una columna
posicion.style.format({"Edad":"{0:,.1f}", "Futbolistas":"${0:,.0f}", "Ratio":"{:.2%}"}).bar(subset="Edad", color="Steelblue")

# Funcion melt
# para mostrar una tabla en formato compacto a formato tabular con los datos repetidos
Tabla_dinamica_body = Tabla_dinamica_body.reset_index()
Tabla_dinamica_body.melt(id_vars=["Body type", "Real face"])
