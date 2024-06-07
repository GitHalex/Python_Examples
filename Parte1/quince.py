""" lista = [int(input("Ingrese un numero: ")) for i in range(5)]
print(lista) """

""" listaEstaturas = [float(input("Ingrese la estatura en metros: ")) for i in range(5)]
print(listaEstaturas)
promedio = sum(listaEstaturas) / len(listaEstaturas)
print(promedio)
altasPromedio = 0
for estatura in listaEstaturas:
  if estatura >= promedio:
    altasPromedio += 1

print(f"Cantidad de personas mayores o igaules al promedio: {altasPromedio}") """

sueldos = [
    [int(input("Ingrese los sueldos para la mañana: ")) for i in range(4)], 
    [int(input("Ingrese los sueldos para la tarde: ")) for i in range(4)]
]

etiquetas = ["Mañana", "Tarde"]

sueldos_etiquetados = list(zip(etiquetas, sueldos))

print(sueldos_etiquetados)



