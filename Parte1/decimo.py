n = int(input("Cuantos triangulos procesaras: "))
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
print(cantidad)
