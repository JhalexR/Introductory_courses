from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://clouditeducation.com/pruebas/")

# importar by para buscar elementos en la pagina con selenium
from selenium.webdriver.common.by import By

# buscar un elemento por ID
elemento = driver.find_element(By.ID,"noImportante")
if elemento is not None:
    print("El elemento por ID fue encontrado")

# buscar un elemento por NAME
elemento = driver.find_element(By.NAME,"ultimo")
if elemento is not None:
    print("El elemento por Name fue encontrado")

# buscar elemento por Xpath
elemento = driver.find_element(By.XPATH,"//tr[@id='noImportante']/td[1]") 
if elemento is not None:
    print("El elemento POR Xpath fue encontrado")
# para saber el xpath debemos buscarlo en  el navegador:
# F12
# Herramienta de seleccion
# seleccionamos la parte que queremos saber el Xpath
# el panel o consola de desarrollador muestra su ubicacion en el HTML
# en el HTML le damos click derecho a la parte que queremos saber xpath
# le damos la opcion copiar -> xpath

# buscar elemento por nombre de clase
elemento = driver.find_element(By.CLASS_NAME,"rojo") 
if elemento is not None:
    print("El elemento por nombre de clase fue encontrado")

# buscar por texto espeficio 
elemento = driver.find_element(By.LINK_TEXT,"Pagina 2") 
if elemento is not None:
    print("El elemento por texto fue encontrado")

# buscar por texto parcial
elemento = driver.find_element(By.PARTIAL_LINK_TEXT,"agina") 
if elemento is not None:
    print("El elemento por texto parcial fue encontrado")

# buscar por tag name
elemento = driver.find_element(By.TAG_NAME,"h3") 
if elemento is not None:
    print("El elemento por tag name fue encontrado")

# buscar por CSS Selector
elemento = driver.find_element(By.CSS_SELECTOR,"#primera") 
if elemento is not None:
    print("El elemento por CSS Selector fue encontrado")

# buscar por mas de un elemento
# buscar por mas de un elemento por Xpath
elemento = driver.find_elements(By.XPATH,"//tr") 
if elemento is not None:
    # se usa para contar la cantidad de elementos encontrados
    print("Se encontraron:",len(elemento),"elementos" )

# buscar por mas de un elemento por tag name
elemento = driver.find_elements(By.TAG_NAME,"tr") 
if elemento is not None:
    # se usa para contar la cantidad de elementos encontrados
    print("Se encontraron:",len(elemento),"elementos" )

# importar time para usar tiempos en el programa
import time

# Acciones

# Click a botones de seleccion y casillas de seleccion

# Click a botones de seleccion
# usamos ID para actuar realizar la accion en es elemento por lo cual tenemos que buscar el nombre del ID
elemento = driver.find_element(By.ID,"RadioGroup1_0")
if elemento is not None:
    elemento.click()

#esperamos 5 sergundos para dar click al siguiente elemento
time.sleep(1)

# usamos ID para actuar realizar la accion en es elemento por lo cual tenemos que buscar el nombre del ID
elemento = driver.find_element(By.ID,"RadioGroup1_1")
if elemento is not None:
    elemento.click()

#esperamos 5 sergundos para dar click al siguiente elemento
time.sleep(1)

# Click a cassillas de seleccion
# usamos ID para actuar realizar la accion en es elemento por lo cual tenemos que buscar el nombre del ID
elemento = driver.find_element(By.ID,"CheckboxGroup1_0")
if elemento is not None:
    elemento.click()

#esperamos 5 sergundos para dar click al siguiente elemento
time.sleep(1)

# usamos ID para actuar realizar la accion en es elemento por lo cual tenemos que buscar el nombre del ID
elemento = driver.find_element(By.ID,"CheckboxGroup1_1")
if elemento is not None:
    elemento.click()

# hacer click en un elemento 
# En HTML el elemento <a> representa un link en este caso estamos buscando un link que diga "Pagina 2" para hacer click en el
# y nos lleve a la siguiente pagina, para facilitar el proceso usamos la funcion "Contains"
elemento = driver.find_element(By.XPATH,"//a[contains(text(),'Pagina 2')]") 
if elemento is not None:
    elemento.click()

# en esta segunda parte del ejercicio despues de que le demos click en link de segunda pagina 
# queremos escribir en una de las cajas de texto de la "pagina 2" el nombre "Juan" 
# hacer click en un elemento 
elemento = driver.find_element(By.ID,"Segundo") 
if elemento is not None:
    elemento.send_keys("Juan")
#esperamos 5 sergundos para dar click al siguiente elemento
time.sleep(1)

# volvemos a la pagina anterior con el mismo metodo de la primera
elemento = driver.find_element(By.XPATH,"//a[contains(text(),'Home')]") 
if elemento is not None:
    elemento.click()

#esperamos 5 sergundos para dar click al siguiente elemento
time.sleep(1)

# Seleccionar de un drop down y lista de seleccion multiple

# Los drop down y lista de seleccion multiple deben ir en un elemento "select" 
# que debe ser un elemento de seleccion

# Clase Select de Selenium
# deselect_all() -> en elementos de seleccion mutiple deselecciona todas las opciones
# deselect_by_index(index) -> remueve la seleccion basado en la posicion o indice
# deselect_by_value(value) -> remueve la seleccion basado en el valor de la seleccion
# deselect_by_visible_text(text) -> remueve la seleccion basado en el texto desplegado
# select_by_index(index) -> Selecciona basado en la posicion o indice
# select_by_value(value) -> Selecciona basado en el valor de la seleccion
# select_by_visible_text(text) -> Selecciona basado en el texto desplegado

# importar libreria para manejo de clase select de Selenium
from selenium.webdriver.support.select import Select

# select_by_value
# En esta parte queremos en el elemento de seleccion multiple lalamdo "ingrediente"
# Seleccionar la opcion "Cebolla"
elemento = driver.find_element(By.NAME,"ingrediente")
if elemento is not None:
    IngredientesSel = Select(elemento)
    IngredientesSel.select_by_value("cebolla")

# select_by_index
# select_by_visible_text
# En esta parte queremos en el elemento de seleccion multiple llamado "Select1"
# Seleccionar la opcion "Platano"
elemento = driver.find_element(By.NAME,"Select1")
if elemento is not None:
    IngredientesSel2 = Select(elemento)
    IngredientesSel2.select_by_index(1) # el elemento en la seleccion multiple en el indice 1 corresponde a "Platano" 
    IngredientesSel2.select_by_visible_text("Sandia") # Buscamos por texto "Sandia"

# Obteniendo un atributo o texto
# varios de los elementos HTML tienen como atributo texto
# si necesitamos obtener ese texto usamos ".text" del Xpath del elemento
elemento = driver.find_elements(By.XPATH,"//*[@id='noImportante']/td[2]") 
if elemento:
    # Accede al primer elemento de la lista y obtiene su texto
    texto = elemento[0].text
    print("Texto:", texto)
else:
    print("No se encontraron elementos.")

# buscar atributo con ID en este caso ID "importante" 
# usando function get_attribute obtenemos nombre de la clase
elemento = driver.find_element(By.ID,"importante") 
if elemento is not None:
    elemento = elemento.get_attribute("Class")
    print("Clase:",elemento)



# propiedades de la clase webdriver para cambiarse de pagina
# currente_url -> URL de la pagina
# currente_window_handle -> handle de la ventana actual
# name -> nombre del navegador
# orientation -> orientacion del dispositivo
# page_source -> Codigo de la pagina
# title -> titulo de la pagina
# windows_handle -> Todos los handles de todas las ventasna de la sesion actual

# handle es un numero de referencia de ventanas

# para cambiarnos a una nueva ventana
# swithc_to.window()
# swithc_to.alert()
# swithc_to.trame()

# Cambiando el foco a una ventana
# primero encuentra la ventana actual
parentHandle = driver.current_window_handle
print("Parent principal", parentHandle)

# encontrar el boton submit y dar click 
elemento = driver.find_element(By.ID,"Buton1")
elemento.click()
time.sleep(3)

# encontrar todos los handles
todoshandles = driver.window_handles
print("todos los handles", todoshandles)

# recorrer las ventasnas con el ciclo hasta llegar a la ventana diferente a la actual
for handle in todoshandles:
    if handle != parentHandle:
        driver.switch_to.window(handle)

# ingresar datos 
elemento = driver.find_element(By.ID,"Segundo")
if elemento is not None:
    elemento.send_keys("Juan")

# guardar en variable la ventana actual 
secondhandle = driver.current_window_handle
print("Parent secundario", secondhandle)

# recorrer las ventasnas con el ciclo hasta llegar a la ventana diferente a la actual
for handle in todoshandles:
    if handle != secondhandle:
        driver.switch_to.window(handle)

# cambiando el foco a una alerta
# se debe buscar el xpath de la alerta 
elemento = driver.find_elements(By.ID,"center") 
elemento.click()
time.sleep(3)

alerta = driver.switch_to.alerta
alerta.accept()


time.sleep(1)
driver.quit()