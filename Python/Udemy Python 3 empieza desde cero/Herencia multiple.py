# Herencia multiple 

# creacion de la clase
class Coche: 
    # crear atributos de la clase
    marca = ""
    color = "Blanco"
    encendido = False
    velocidad = 0

    # definición de los atributos 
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color  

    # Creacion y definicion de función
    def encender(self):
        self.encendido = True

    # Creacion y definicion de función con argumentos
    def velocimetro(self, velocidad):
        self.velocidad = velocidad

# segunda clase creada
class coche4x4:
    size_ruedas = 19

# nueva clase que va heredar atributos y metodos de la primera y segunda clase
class Coche_deportivo(Coche, coche4x4):  # se colocan el nombre de las dos clases para heredar
    cv = 60

    # definición de los atributos nueva clase
    def __init__(self, marca, color, cv, size_ruedas):
        self.marca = marca
        self.color = color 
        self.cv = cv # nuevo atributo que solo posee la nueva clase
        self.size_ruedas = size_ruedas

# aca se demuestra que hereda los atributos
print (Coche_deportivo.size_ruedas)