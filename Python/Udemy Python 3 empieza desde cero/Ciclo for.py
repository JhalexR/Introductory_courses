numeros = [1, 55, 88, 43, 65, 90, 100]

# en el ciclo for se declara una variable que almacena el contenido del 
# vector en ella (num) mientras va avanzando automaticamente en las posiciones
# sin necesidad de declarar el incremento +1 

for num in numeros:
    print(num)

# ejemplo for tablas de multiplicar

tabla = int(input('¿Que tabla quieres ver?: '))
nums_range = range(0,11)

for num in nums_range:
    result = tabla*num
    print(f'{tabla} * {num} = {result}')