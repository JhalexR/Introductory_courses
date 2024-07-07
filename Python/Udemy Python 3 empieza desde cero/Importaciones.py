
# al utilizar from traemos las clases o partes especificas de ese archivo
from Clases.Coches import Coche, Coche_deportivo

# si usamos la pabra import sin el from traemos todas las clases
import Clases.Coches

# es necesario cuando vayamos a importar colocar la ruta 
# donde esta el archivo con las clases colocar la ruta
# en este caso el archivo esta en la carpeta Clases por ello
# se escribe import o from Clases.Coches

# aca se demuestra que trae desde el archivo con las clases
# las clases para poderlas usar en este codigo

# muestra un atributo de la primera clase
print (Coche.color)

# muestra  nuevo atributo de la nueva clase
print (Coche_deportivo.cv)



