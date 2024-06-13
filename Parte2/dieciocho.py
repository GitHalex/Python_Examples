""" nombres = []
for x in range(5):
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)

print(f"Lista de nombres\n{nombres}")

# Algoritmo de burbuja para ordenar la lista
for i in range(len(nombres) - 1):
    for j in range(len(nombres) - 1 - i):
        if nombres[j] > nombres[j + 1]:
            nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]

print(f"Lista de nombres ordenada alfabéticamente\n{nombres}") """

""" cantidad_empleados = int(input("Ingrese la cantidad de empleados: "))
nombres_trabajadores = []
sueldos_trabajadores = []
for i in range(cantidad_empleados):
  nombre = input("Ingrese un nombre: ")
  nombres_trabajadores.append(nombre)
  sueldo = int(input("Ingrese su sueldo: "))
  sueldos_trabajadores.append(sueldo)

print(nombres_trabajadores)
print(sueldos_trabajadores)
print(f"Utilizando con el metodo sorted seria: {sorted(sueldos_trabajadores)}")

for i in range(len(sueldos_trabajadores) - 1):
  for j in range(len(sueldos_trabajadores) - 1 -i):
    if sueldos_trabajadores[j] > sueldos_trabajadores[j + 1]:
      sueldos_trabajadores[j], sueldos_trabajadores[j + 1] = sueldos_trabajadores[j + 1], sueldos_trabajadores[j]

print(f"Lista de los sueldos ordenados: {sueldos_trabajadores}") """


my_list = [int(input("Ingrese un numero: ")) for i in range(5)]
swapped = True

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nOrdenada:")
print(my_list)

""" my_list.reverse()
print(f"Usando el metodo reverse en la lista: {my_list}") """

for i in range(len(my_list) -1):
    for j in range(len(my_list) - 1 -i):
        if my_list[j] < my_list[j + 1]:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

print(f"Lista donde la esta de mayor a menor: {my_list}")