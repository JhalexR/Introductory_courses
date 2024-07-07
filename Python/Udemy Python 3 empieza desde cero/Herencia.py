# Herencia

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

# nueva clase que va heredar atributos y mnetodos de la primera
class Coche_deportivo(Coche):  # para heredar colocar (clase de la que se va heredar) 
    cv = 60

    # definición de los atributos nueva clase
    def __init__(self, marca, color, cv):
        self.marca = marca
        self.color = color 
        self.cv = cv # nuevo atributo que solo posee la nueva clase

# aca se demuestra que hereda los atributos
print (Coche_deportivo.color)

# muestra del nuevo atributo de la nueva clase
print (Coche_deportivo.cv)

# ejemplo se crea un objeto de la primera clase 
coche1 = Coche("seat","negro")

# se puede añadir a ese objeto los atributos de la nueva clase
coche1 = Coche_deportivo("BMW","Rojo",260)

# se comprueban los nuevos atributos
print (coche1.marca)
print (coche1.color)
print (coche1.cv)