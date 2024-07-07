# Encapsulamiento

# Encapsulamiento en Python
# En Python, el encapsulamiento se logra mediante convenciones de nombres
# y la implementación de métodos. 
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

# Atributos Públicos: nombre es un atributo público y se puede
# acceder directamente desde fuera de la clase.
print(persona.nombre)  # Salida: Juan

# Atributos Protegidos: _edad es un atributo protegido. 
# Por convención, no debería ser accedido directamente desde fuera de la clase, 
# aunque Python lo permite. (se puede, pero no se recomienda)
print(persona._edad)  # Salida: 30

# Atributos Privados: __salario es un atributo privado. 
# No se puede acceder directamente desde fuera de la clase.
# al intentar acceder a un atributo privado esto generará un error
# print(persona.__salario)  # AttributeError

# acceso_salario es un método público que llama 
# al método privado __mostrar_salario.
# Acceder al atributo privado mediante un método público
print(persona.acceso_salario())  # Salida: 50000

# Acceso a un método protegido (se puede, pero no se recomienda)
print(persona._mostrar_edad())  # Salida: 30

# __mostrar_salario es un método privado, que no se puede llamar
# directamente desde fuera de la clase.
# Intentar acceder a un método privado (esto generará un error)
# print(persona.__mostrar_salario())  # AttributeError

# Name Mangling
# Python aplica una técnica llamada name mangling para atributos y métodos privados, 
# lo que renombra internamente estos atributos y métodos para evitar colisiones. 
# Por ejemplo, __salario se renombra internamente como _Persona__salario. 
# Aunque se puede acceder a estos atributos y métodos renombrados, 
# no es una práctica recomendada.

# Acceso a un atributo privado utilizando name mangling
print(persona._Persona__salario)  # Salida: 50000

#El encapsulamiento en Python es una forma eficaz de proteger 
# los datos y asegurarse de que solo se acceda a ellos de manera controlada,
# a través de métodos definidos en la clase. 
# Esto ayuda a mantener la integridad de los datos y a seguir el principio 
# de ocultación de información en la programación orientada a objetos.