""" Desarrollar un programa con dos funciones. La primer solicite el ingreso de un entero y muestre el cuadrado de dicho valor. La segunda que solicite la carga de dos valores y muestre el producto de los mismos. LLamar desde el bloque del programa principal a ambas funciones. """

""" def alCuadrado() -> int:
  numero = int(input("Ingrese un numero: "))
  return numero**2

def producto() -> float:
  num1 = int(input("numero1: "))
  num2 = int(input("numero2: "))
  return num1*num2

print(alCuadrado())
print(producto())  """

""" Desarrollar un programa que solicite la carga de tres valores y muestre el menor. Desde el bloque principal del programa llamar 2 veces a dicha función (sin utilizar una estructura repetitiva) """

def valores() -> int: 
    numero1 = int(input("Dame un numero 1: "))
    numero2 = int(input("Dame un numero 2: "))
    numero3 = int(input("Dame un numero 3: "))

    candidato = numero1

    if numero2 < candidato:
        candidato = numero2
      
    if numero3 < candidato:
        candidato = numero3
    
    return candidato
   
print(valores())

