# Encapsulamiento

# Encapsulamiento en Python
# En Python, el encapsulamiento se logra mediante convenciones de nombres
#  y la implementación de métodos. 
# Existen tres niveles de acceso a los atributos y métodos de una clase:

# Público (Public): Atributos y métodos que están disponibles desde fuera de la clase. 
# Se definen sin guiones bajos al principio del nombre.

# Protegido (Protected): Atributos y métodos que no deberían ser accesibles desde fuera de la clase, 
# pero que aún pueden ser accedidos. 
# Se definen con un guion bajo _ al principio del nombre.

# Privado (Private): Atributos y métodos que no son accesibles desde fuera de la clase.
# Se definen con dos guiones bajos __ al principio del nombre.

# Ejemplo de Encapsulamiento en Python

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo público
        self._edad = edad     # Atributo protegido
        self.__salario = 50000  # Atributo privado

    def mostrar_nombre(self):
        return self.nombre

    def _mostrar_edad(self):
        return self._edad

    def __mostrar_salario(self):
        return self.__salario

    def acceso_salario(self):
        return self.__mostrar_salario()  # Método público que accede a un método privado


# Crear una instancia de la clase Persona
persona = Persona("Juan", 30)

# Acceso a un atributo público
print(persona.nombre)  # Salida: Juan

# Acceso a un atributo protegido (se puede, pero no se recomienda)
print(persona._edad)  # Salida: 30

# Intentar acceder a un atributo privado (esto generará un error)
# print(persona.__salario)  # AttributeError

# Acceder al atributo privado mediante un método público
print(persona.acceso_salario())  # Salida: 50000

# Acceso a un método protegido (se puede, pero no se recomienda)
print(persona._mostrar_edad())  # Salida: 30

# Intentar acceder a un método privado (esto generará un error)
# print(persona.__mostrar_salario())  # AttributeError
