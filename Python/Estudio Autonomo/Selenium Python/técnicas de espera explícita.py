# Cuando usas Selenium para hacer clic en un enlace que navega a otra página, 
# el script no espera automáticamente hasta que la nueva página se cargue por completo 
# antes de ejecutar la siguiente acción. 

# Esto puede causar errores si intentas interactuar con elementos en la nueva página 
# antes de que estén disponibles. Para manejar esto, 
# puedes usar las técnicas de espera explícita que ofrece Selenium.

# Las esperas explícitas permiten pausar el script hasta que se cumpla una condición específica, 
# como la presencia de un elemento en la nueva página.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializa el navegador (asegúrate de tener el driver correcto para tu navegador)
driver = webdriver.Chrome()

# Navega a la página inicial
driver.get('http://pagina-inicial.com')

# Encuentra el elemento y haz clic en el enlace
enlace = driver.find_element(By.LINK_TEXT, 'Texto del enlace')
enlace.click()

# Espera explícita hasta que el elemento de la nueva página esté presente
try:
    elemento = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'id-del-elemento'))
    )
    # Realiza la acción deseada con el elemento encontrado
    elemento.send_keys('Texto a ingresar')
except TimeoutException:
    print("El elemento no se encontró en la nueva página dentro del tiempo esperado")

# Cierra el navegador
driver.quit()

# Se utiliza una espera explícita (WebDriverWait) 
# para esperar hasta que el elemento de la nueva página esté presente 
# (en este caso, se busca por ID, pero puedes usar cualquier localizador que necesites).

# Una vez que el elemento está presente, se realiza la acción send_keys.

# La espera explícita espera hasta 10 segundos (WebDriverWait(driver, 10)) por defecto, 
# pero puedes ajustar este tiempo según sea necesario. 

# Si el elemento no se encuentra en el tiempo especificado, se lanza una TimeoutException,
# que puedes manejar para evitar que el script falle abruptamente.