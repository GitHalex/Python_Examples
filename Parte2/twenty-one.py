#odds = [x for x in squares if x % 2 != 0 ]

""" paises = []
temperaturas = []
for i in range(3):
  pais = input("Ingrese un pais: ")
  paises.append(pais)
  temp1 = float(input("Ingrese la temperatura media 1: "))
  temp2 = float(input("Ingrese la temperatura media 2: "))
  temp3 = float(input("Ingrese la temperatura media 3: "))
  temperaturas.append([temp1, temp2, temp3])

print("Imprimir las listas")
for k in range(3):
  print(f"Pais: {paises[k]} => temperaturas: {temperaturas[k]}")

media_total = []
for j in range(3):
  media = (temperaturas[j][0] + temperaturas[j][1] + temperaturas[j][2]) / 3
  media_total.append(media)

print("Imprimir las listas")
for m in range(3):
  print(f"Pais: {paises[m]} => temperatura media: {media_total[m]}")


paisMayor = paises[0]
temperaturaMayor = media_total[0]
for x in range(1, 3):
   if temperaturaMayor < media_total[x]:
      temperaturaMayor = media_total[x]
      paisMayor = paises[x]

print(paisMayor, temperaturaMayor) """



# Definir las listas
""" empleados = []
inasistencias = []

# Solicitar los nombres de los empleados y sus días de inasistencia
for i in range(3):
    nombre = input("Ingrese el nombre del empleado: ")
    empleados.append(nombre)
    faltas = input(f"Ingrese los días del mes que {nombre} faltó (separados por comas): ")
    faltas_list = [int(dia) for dia in faltas.split(",")]
    inasistencias.append(faltas_list)

# Imprimir los nombres de los empleados y los días que faltaron
print("\nInasistencias de empleados:")
for i in range(3):
    print(f"Empleado: {empleados[i]} => Días que faltó: {inasistencias[i]}")

# Mostrar los empleados con la cantidad de inasistencias
print("\nCantidad de inasistencias:")
cantidad_inasistencias = [len(faltas) for faltas in inasistencias]
for i in range(3):
    print(f"Empleado: {empleados[i]} => Cantidad de inasistencias: {cantidad_inasistencias[i]}")

# Mostrar el nombre o los nombres de empleados que faltaron menos días
min_inasistencias = min(cantidad_inasistencias)
empleados_menos_faltas = [empleados[i] for i in range(3) if cantidad_inasistencias[i] == min_inasistencias]

print("\nEmpleado(s) que faltó(aron) menos días:")
for empleado in empleados_menos_faltas:
    print(empleado) """


# Inicializar la lista principal
lista_principal = []

# Crear las sublistas y agregarlas a la lista principal
for i in range(1, 51):
    sublista = list(range(1, i + 1))
    lista_principal.append(sublista)

# Imprimir la lista principal para verificar el resultado
for sublista in lista_principal:
    print(sublista)
