""" def promedio(num1: int, num2: int, num3: int) -> float:

  suma = num1 + num2 + num3
  promedio = suma / 3

  return round(promedio, 2)

numero1 = int(input("primer numero: "))
numero2 = int(input("segundo numero: "))
numero3 = int(input("tercer numero: "))

print(promedio(numero1, numero2, numero3)) """


""" def perimetroCuadrado(lado: int=2) -> int:

  return lado*4


lado = int(input("Ingrese un lado: "))

print(perimetroCuadrado(lado))
print(perimetroCuadrado()) """


def superficie(ancho: int, alto: int) -> int:

  superficie = ancho*2 + alto*2

  return superficie

anchoPri = int(input("Ingrese un numero primero: "))
altoPri = int(input("Ingrese un numero primero: "))
anchoSec = int(input("Ingrese un numero segundo: "))
altoSec = int(input("Ingrese un numero segundo: "))

primerSuperficie = superficie(anchoPri, altoPri)
segundoSuperficie = superficie(anchoSec, altoSec)

if primerSuperficie > segundoSuperficie:
  print(f"El primer rectangulo: {primerSuperficie} es mas grande que el segundo: {segundoSuperficie}")
else:
  print(f"El segundo rectangulo: {segundoSuperficie} es mas grande que el primero: {primerSuperficie}")