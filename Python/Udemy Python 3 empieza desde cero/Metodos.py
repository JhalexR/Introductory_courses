# Metodos de objetos

# creacion de la clase
class Coche: 
    # crear atributos de la clase
    marca = ""
    color = "Blanco"
    encendido = False
    velocidad = 0

    # definición de los atributos 
    def __init__(self, marca, color) -> None:
        self.marca = marca
        self.color = color  

    # Creacion y definicion de función
    def encender(self):
        self.encendido = True

    # Creacion y definicion de función con argumentos
    def velocimetro(self, velocidad):
        self.velocidad = velocidad

# creacion de objetos 
coche1 = Coche("seat","negro")
coche_lujo = Coche("BMW", "Plateado")

# usar metodo creado para el objeto
coche1.encender()

# se uso el metodo de la clase solo para uno de los 
# dos objetos creados
print(coche1.encendido)
print(coche_lujo.encendido)

# solicitar velocidad al usuario
velocidad = int(input('cual es la velocidad del auto? '))

# invocar metodo velocidad con llevando el argumento
coche1.velocimetro(velocidad)

# muestra velocidad del coche ingresada por usuario
print(coche1.velocidad)