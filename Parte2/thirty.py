def cantidadMayores(num1: int, num2: int, num3: int, num4: int) -> int:

  contador = 0
  if num1 >= 18:
    contador += 1
  if num2 >= 18:
    contador += 1
  if num3 >= 18:
    contador += 1
  if num4 >= 18:
    contador += 1

  return contador
edades = [int(input("Ingrese una edad: ")) for i in range(4)]
mayoresDeEdad=cantidadMayores(*edades)
print(f"de la lista: {edades} son {mayoresDeEdad} mayores de edad")