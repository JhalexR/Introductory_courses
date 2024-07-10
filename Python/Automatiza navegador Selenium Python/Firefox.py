from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://clouditeducation.com/pruebas/")

# importar by para buscar elementos en la pagina con selenium
from selenium.webdriver.common.by import By
elemento = driver.find_element(By.ID,"noImportante")
if elemento is not None:
    print("El elemento fue encontrado")

# importar time para usr tiempos en el programa
import time
time.sleep(5)
driver.quit()
