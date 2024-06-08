""" nombres = [input("Ingrese un nombre: ") for i in range(5)]
menor = nombres[0]

for nombre in nombres:
    if nombre < menor:
        menor = nombre

lista_orden_menor = [menor]

print(lista_orden_menor) """


# Cargar la lista con 5 elementos enteros
numeros = [int(input("Ingrese un número entero: ")) for _ in range(5)]

# Encontrar el mayor valor en la lista
# mayor = max(numeros)

mayor = numeros[0]
for numero in range(len(numeros)):
    if numeros[numero] > mayor:
        mayor = numeros[numero]

# Contar cuántas veces se repite el mayor valor en la lista
repeticiones = numeros.count(mayor)

# Imprimir el mayor valor
print(f"El mayor valor es: {mayor}")

# Imprimir un mensaje si el mayor valor se repite
if repeticiones > 1:
    print(f"El mayor valor se repite {repeticiones} veces.")
else:
    print("El mayor valor no se repite.")

