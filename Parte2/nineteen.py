""" alumnos  = []
notas = []
for x in range(5):
  nombre = input("Ingrese el numero del Alumno: ")
  alumnos.append(nombre)
  nota = int(input("Ingrese la nota de dicho alumno: "))
  notas.append(nota)


for k in range(4):
  for x in range(4-k):
    if notas[x] < notas[x + 1]:
      aux1 = notas[x]
      notas[x] = notas[x + 1]
      aux2 = alumnos[x]
      alumnos[x] = alumnos[x + 1]
      alumnos[x + 1] = aux2

print("Lista de alumnos y sus notas ordenadas de mayor a menor")

for x in range(5):
  print(alumnos[x], notas[x]) """



paises = []
cant_habitantes = []

for i in range(5):
  pais = input("Ingrese un pais: ")
  paises.append(pais)
  cantidad = int(input("Ingrese la cantidad de habitantes: "))
  cant_habitantes.append(cantidad)


for i in range(len(paises) - 1):
  for j in range(len(paises) - 1 - i):
    if paises[j] > paises[j + 1]:
      paises[j], paises[j + 1] = paises[j + 1], paises[j]
      cant_habitantes[j], cant_habitantes[j + 1] = cant_habitantes[j + 1], cant_habitantes[j]

print("Respecto al orden alfabetico")
for k in range(len(paises)):
  print(f"pais {paises[k]} => habitantes {cant_habitantes[k]} Millones")



for i in range(len(cant_habitantes) - 1):
  for j in range(len(cant_habitantes) - 1 - i):
    if cant_habitantes[j] < cant_habitantes[j + 1]:
      cant_habitantes[j], cant_habitantes[j + 1] = cant_habitantes[j + 1], cant_habitantes[j]
      paises[j], paises[j + 1] = paises[j + 1], paises[j]
print("")
print("Respecto a los habitantes de mayor a menor")
for l in range(len(cant_habitantes)):
  print(f"pais {paises[l]} => habitantes {cant_habitantes[l]} Millones")
  