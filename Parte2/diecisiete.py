frutas = []
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
    print(f"Producto: {frutas[i]} --> Precio: {precios[i]}")
