# calculadora en base a los numeros de entrada
num1 = int(input("ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

if (num1 > num2):
    print(f"La suma es {num1+num2}")
    print(f"La resta es {num1-num2}")
else:
    print(f"El producto es {num1*num2}")
    print(f"La division es {num1/num2}")


""" nota1 = int(input("Nota 1:"))
nota2 = int(input("Nota 2:"))
nota3 = int(input("Nota 3:"))

suma = nota1 + nota2 + nota3
promedio = suma / 3
if (promedio >= 7):
    print("Promocionado")
else:
    print("Perri no te alcanza la nota9") """

numero = int(input("ingrese un numero: "))
if numero >= 0 and numero <= 9:
    print(f"El numero tiene un digito {numero}")
elif numero >= 10 and numero <= 99:
    print(f"El  numero tiene dos digitos {numero}")
else:
    print(f"Me introduciste cualquier webada {numero}")
