nombres = []
for x in range(5):
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)

print(f"Lista de nombres\n{nombres}")

# Algoritmo de burbuja para ordenar la lista
for i in range(len(nombres) - 1):
    for j in range(len(nombres) - 1 - i):
        if nombres[j] > nombres[j + 1]:
            nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]

print(f"Lista de nombres ordenada alfabéticamente\n{nombres}")
