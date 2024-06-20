def promedio(num1: int, num2: int, num3: int) -> float:

  suma = num1 + num2 + num3
  promedio = suma / 3

  return round(promedio, 2)

numero1 = int(input("primer numero: "))
numero2 = int(input("segundo numero: "))
numero3 = int(input("tercer numero: "))

print(promedio(numero1, numero2, numero3))