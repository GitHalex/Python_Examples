""" listaNumeros = [101, 20, 300, 400, 100, 200, 3, 6, 7]
numerosMayor = 0
for numero in listaNumeros:
  if numero > 100:
    numerosMayor += 1

print(f"Cantidad de numeros mayores a 100 son: {numerosMayor}") """


""" for i in range(5):
  numero = int(input("Ingrese un numero: "))
  if numero >= 7:
    print(numero) """

nombres = ["Alex", "Ricardo", "Jorge", "Pijas", "Adan"]
nombres_cinco = 0
for nombre in nombres:
  if len(nombre) >= 5:
    nombres_cinco += 1
print(nombres_cinco)