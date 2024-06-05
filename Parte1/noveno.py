""" x = 1
altas = 0
bajas = 0
while x  <= 10:
   nota = int(input("Ingrese 10 notas: "))
   if nota >= 7:
      altas += 1
   else:
      bajas += 1

   x = x+1

print(f"{altas} cantidad de notas altas")
print(f"{bajas} cantidad de notas bajas") """


""" n = int(input("Ingrese la cantidad de personas a procesar"))
x = 1
suma = 0
while x <= n:
   altura = float(input("inggrese la altura:"))
   suma = suma + altura
   x += 1

print(f"{suma/n} promedio de estatura") """

""" cantidad_empleados = int(input("Ingrese la cantidad de empleados: "))
x = 1
empleados_100_300 = 0
empleados_mas_300 = 0
sueldo_empresa = 0
while x <= cantidad_empleados:
   sueldo = int(input("Ingrese un sueldo de un empleado: "))
   if sueldo >= 100 and sueldo <= 500:
      x = x +1
      if sueldo >= 100 and sueldo <=300:
         empleados_100_300 += 1
         sueldo_empresa += sueldo 
      else:
         empleados_mas_300 += 1
         sueldo_empresa += sueldo

print(f"{empleados_100_300} cantidad de empleados que reciben un sueldo de 100-300 ") 
print(f" {empleados_mas_300} cantidad de empleados que reciben un sueldo mas de 300") 
print(f"Dinero que se gasta en sueldos {sueldo_empresa} pelucholares") """

"""
x = 1
contador = 0
valor_once = 11
while x <= 25:
   print(valor_once*x, end="-")
   contador += 1
   x += 1

print(contador)"""


multiplos = 8
while multiplos <= 500:
    if multiplos % 8 == 0:
      print(multiplos, end=" - ")
    multiplos += 1

""" suma1 = 0
suma2 = 0
x=1
print("Carga de la primera lista")
while x <= 15:
   valor = int(input("Ingrese un valor"))
   suma1 += valor
   x += 1

x= 1
print("Carga de la segunda lista")
while x <= 15:
   valor = int(input("Ingrese un valor"))
   suma2 += valor
   x += 1

if suma1 > suma2:
   print("La lista 1 tiene un valor acumulado mayor")
elif suma2 > suma1:
    print("La lista 2 tiene un valor acumulado mayor")
else:
   print("Ambas listas tienen valores iguales") """

"""
x = 1
n = int(input("Ingrese cantidad de numeros: "))
pares = 0
impares = 0
while x <= n:
   valor = int(input("Ingrese un numero: "))
   if valor % 2 == 0:
      pares +=1
   else:
      impares +=1
   x+= 1

print(f"En una cantidad de numeros: {n}")
print(f"existe: {pares} numeros pares")
print(f"existe: {impares} numeros impares")"""















































 







































