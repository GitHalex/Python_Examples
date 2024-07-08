from operacioneslista import cargar, imprimir_mayor, imprimir_suma

lista = cargar()
imprimir_mayor(lista)
imprimir_suma(lista)

#Las funciones del modulo operacioneslista todas la lista trabaja con 5 elementos ojo perri
#Pro si trabajamos la definicion con el rango de tamaño puede aceptar cualquier tamaño
listaOtra = [int(input("Ingrese un numero: ")) for _ in range(3)]

imprimir_mayor(listaOtra)
imprimir_suma(listaOtra)
