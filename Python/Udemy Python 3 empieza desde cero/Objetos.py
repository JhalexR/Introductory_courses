# programacion orientada a objetos

# creacion de la clase
class Coche: 
    # crear atributos de la clase
    marca = ""
    color = "Blanco"
    # para construir una clase vacia se usa la palabra reservada "pass"

    # definición de los atributos 
    def __init__(self, marca, color) -> None:
        self.marca = marca
        self.color = color    

# creacion del objeto
coche1 = Coche("seat","negro")

# creacion del segundo objeto
coche_lujo = Coche("BMW", "Plateado")

# acceder a los atributos de un objeto
print(coche1.marca)
print(coche1.color)
print(coche_lujo.marca)
print(coche_lujo.color)

# acceder a los atributos de un objeto y cambiar su valor
coche1.marca = "Ford"
print(coche1.marca)