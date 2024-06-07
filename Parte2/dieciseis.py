nombres = [input("Ingrese un nombre: ") for i in range(5)]
menor = nombres[0]

for nombre in nombres:
    if nombre < menor:
        menor = nombre

lista_orden_menor = [menor]

print(lista_orden_menor)

