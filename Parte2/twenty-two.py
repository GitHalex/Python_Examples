empleados = []
sueldos = []
cantidad_empleados = int(input("Cantidad de empleados: "))
for i in range(cantidad_empleados):
    nombre = input("Ingrese el nombre del empleado: ")
    empleados.append(nombre)
    sueldo = int(input("Ingrese el sueldo: "))
    sueldos.append(sueldo)

# Crear una lista de índices para iterar sobre una copia
indices_a_eliminar = [j for j in range(len(sueldos)) if sueldos[j] > 10000]

# Eliminar elementos desde el final para evitar problemas de índice
for j in sorted(indices_a_eliminar, reverse=True):
    sueldos.pop(j)
    empleados.pop(j)

print("Mostrar listas")
for k in range(len(empleados)):
    print(f"Empleado: {empleados[k]} y su sueldo: {sueldos[k]}")
