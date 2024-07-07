# Clases

# creacion de la clase 1
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

# Creacion clase 2
class Coche_deportivo(Coche):  # para heredar colocar (clase de la que se va heredar) 
    cv = 60

    # definición de los atributos nueva clase
    def __init__(self, marca, color, cv):
        self.marca = marca
        self.color = color 
        self.cv = cv # nuevo atributo que solo posee la nueva clase