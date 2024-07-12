import unittest

# Definimos una función suma que suma dos números.
def suma(a, b):
    return a + b

#Creamos una clase TestSuma que hereda de unittest.TestCase
class TestSuma(unittest.TestCase):

    #Definimos tres métodos de prueba dentro de la clase para 
    # probar diferentes casos de la función suma.
    # Utilizamos assertEqual para verificar que el resultado 
    # de la función es el esperado
    def test_suma_positivos(self):
        self.assertEqual(suma(1, 2), 3)
    
    def test_suma_negativos(self):
        self.assertEqual(suma(-1, -2), -3)
    
    def test_suma_mixtos(self):
        self.assertEqual(suma(-1, 1), 0)

# Ejecutamos las pruebas con unittest.main()
if __name__ == '__main__':
    unittest.main()

# principales características y usos de unittest:

# Organización de pruebas: 
# Permite organizar las pruebas en clases y métodos, 
# lo que facilita la estructuración y el mantenimiento de las mismas.

# Comprobaciones automáticas: 
# Proporciona un conjunto de métodos de aserción (assertions) 
# para verificar que el código produce los resultados esperados. 
# Algunos ejemplos son assertEqual, assertTrue, assertFalse, assertRaises, entre otros.

# Configuración y limpieza: 
# Ofrece métodos como setUp y tearDown que se ejecutan antes y después de cada prueba, 
# respectivamente, para configurar el entorno necesario y limpiar después de las pruebas.

# Ejecución de pruebas: 
# Incluye un ejecutor de pruebas que puede descubrir y ejecutar 
# todas las pruebas en un módulo o paquete.

#Integración con otras herramientas: Es compatible con otras herramientas de testing y frameworks, 
# como pytest y nose, lo que permite extender su funcionalidad.