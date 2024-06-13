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

cantidad_empleados = int(input("Ingrese la cantidad de empleados: "))
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

print(f"Lista de los sueldos ordenados: {sueldos_trabajadores}")
