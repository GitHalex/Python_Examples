""" frutas = []
precios = []
for i in range(5):
  fruta = input("Ingrese una fruta: ")
  frutas.append(fruta)
  precio = float(input("Ingrese un precio: "))
  precios.append(precio) 

primerPrecio = precios[0]
print(f"Primer producto: {frutas[0]}  -->   Precio: {precios[0]}")
for i in range(1, len(precios)):
  if precios[i] >= primerPrecio:
    print(f"Producto: {frutas[i]} --> Precio: {precios[i]}") """



""" nombres = []
notas = []
for i in range(4):
  nombre = input("Ingrese un nombre: ")
  nombres.append(nombre)
  nota = float(input("Ingrese una nota: "))
  notas.append(nota)

contarBuenos = 0
condicion = []
for i in range(len(notas)):
  if notas[i] >= 8:
    condicion.append("Muy Bueno")
    contarBuenos += 1
  elif notas[i] >= 4 and notas[i] < 8:
    condicion.append("Bueno")
  else:
    condicion.append("Insuficiente")

print(nombres)
print(notas)
print(condicion)

print(f"Cantidad de alumos que son muy buenos: {contarBuenos}") """

primeraLista = [int(input("Ingrese un numero a la primera lista: ")) for _ in range(4)]
segundaLista = [int(input("Ingrese un numero a la segunda lista: ")) for _ in range(4)]
sumaLista = [primeraLista[i] + segundaLista[i] for i in range(len(primeraLista))]
print(primeraLista)
print(segundaLista)
print(sumaLista)




















































  