""" n = int(input("Cuantos triangulos procesaras: "))
cantidad = 0
for i in range(n):
    base = int(input("Ingrese el valor de la base: "))
    altura = int(input("Ingrese el valor de la altura: "))
    area = base*altura/2
    print("superficie")
    print(area)
    if area > 12:
        cantidad += 1

print("Cantidad de triangulos con superficie mayor a 12")
print(cantidad) """

""" cantidad = 0
for i in range(1, 11):
    numero = int(input("Dame numeros: "))
    if i > 5:
        cantidad += numero

print(f"La suma de los ultimos cinco es: {cantidad}") """

""" for i in range(5, 51, 5):
    print(i)
 """

""" valor = int(input("ingrese un valor de 1 al 10:"))
if valor >= 1 and valor <= 10:
    for i in range(13):
        print(f"{valor} x {i} = {valor*i}")
else:
    print("ingresaste un numero menor a 1 o mayor a 10") """


""" n = int(input("Ingrese la cantidad de triangulos: "))
equ = 0
iso = 0
esc = 0
for i in range(n):
    lado1 = int(input("Primer lado: "))
    lado2 = int(input("Segundo lado: "))
    lado3 = int(input("Tercer lado: "))

    if lado1 == lado2 and lado1 == lado3:
        equ += 1
    elif lado1 == lado2 or lado1 == lado3:
        iso += 1
    else:
        esc += 1

print(f"Equilatero: {equ}")
print(f"Isosceles: {iso}")
print(f"Ninfuno: {esc}") """

""" negativos = 0
positivos = 0
multiplos = 0
acc_pares = 0
for i in range(10):
    num = int(input("Ingrese un numero: "))
    if num >= 0:
        positivos += 1
        if num % 15 == 0:
            multiplos += 1
        if num % 2 == 0:
            acc_pares += 1
    elif num < 0:
        negativos += 1
        if num % 15 == 0:
            multiplos += 1
        if num % 2 == 0:
            acc_pares += 1

print(f"{negativos}")
print(f"{positivos}")
print(f"multiplos: de 15  {multiplos}")
print(f"Acumulado pares {acc_pares}") """


""" suma_cinco = 0
suma_seis = 0
suma_once = 0
for edad_cinco in range(5):
    cinco = int(input("Ingrese 5 numeros: "))
    suma_cinco += cinco

for edad_seis in range(6):
    seis = int(input("Ingrese 6 numeros: "))
    suma_seis += seis

for edad_once in range(11):
    once = int(input("Ingrese 11 numeros: "))
    suma_once += once

print(f"promedio edad MAÑANA {suma_cinco/5}")
print(f"promedio edad TARDE {suma_seis/6}")
print(f"promedio edad NOCHE {suma_once/11}")

print(F"promedio de los tres turnos {(suma_cinco+suma_seis+suma_once)/22}") """

""" Confeccionar un programa que solicite la carga de102.
valores reales por teclado, mostrar al final su suma """
suma_reales = 0
for i in range(10):
    numero = float(input("Ingrese un numero: "))
    # suma de reales
    suma_reales += numero

# total de la suma de numeros reales
print(suma_reales)
