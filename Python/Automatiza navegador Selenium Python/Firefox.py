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

# Acciones

# hacer click en un elemento 
elemento = driver.find_element(By.XPATH,"//a[contains(text(),'Pagina 2')]") # buscar en la consola con F12 el Xpath para colocarlo
if elemento is not None:
    elemento.click()

# hacer click en un elemento 
elemento = driver.find_element(By.ID,"Segundo") # se dbe buscar antes en la consola el id a donde nos lleva la accion anterior
if elemento is not None:
    elemento.send_keys("Juan")


# importar time para usar tiempos en el programa
import time
time.sleep(5)
driver.quit()