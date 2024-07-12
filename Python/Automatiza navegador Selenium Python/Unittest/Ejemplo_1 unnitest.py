import unittest
from selenium import webdriver

# La librería unittest en Python se utiliza para escribir y ejecutar pruebas unitarias. 
# Las pruebas unitarias son una técnica de testing de software en la que se verifica 
# el correcto funcionamiento de pequeñas partes individuales de un programa, como funciones o métodos. 
# La idea es asegurarse de que cada parte del código funcione correctamente de manera aislada.


class FindByIdName (unittest.TestCase):

    def setUp(self):
        global driver 
        driver = webdriver.Firefox()
        driver.get("http://clouditeducation.com/pruebas/")

    def testIdName(self):
        elementById = driver.find_element_by_id("noImportante")
        if elementById is not None:
            print("Encontramos el elemento con Id = noImportante")

        elementByName = driver.find_element_by_name("ultimo")
        if elementByName is not None:
            print("Encontramos el elemento con name = ultimo")

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
    unittest.main()
