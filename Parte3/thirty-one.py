""" def cargarEnteros()-> list:
   listaEnteros = [int(input("Ingrese un numero entero: ")) for _ in range(5)]
   return listaEnteros

def mayorMenor(listaEnteros: list) -> tuple:
   
  mayor = listaEnteros[0]
  menor = listaEnteros[0]

  for i in range(1, len(listaEnteros)):
    if listaEnteros[i] > mayor:
      mayor = listaEnteros[i]
    if listaEnteros[i] < menor:
      menor = listaEnteros[i]

  return (mayor, menor)

numeros = cargarEnteros()
mayorTupla, menorTupla = mayorMenor(numeros)
print(f"Convertido a tupla: Mayor: {mayorTupla} y Menor: {menorTupla}") """



def nameSueldo() -> tuple:

  name = input("Ingrese un nombre: ")
  sueldo= int(input("Ingrese su sueldo: "))
  return (name, sueldo)

def mayorSueldo(empleado1: tuple, empleado2: tuple) -> str:
  mayorSueldo = empleado1[1]
  if mayorSueldo < empleado2[1]:
    # mayorSueldo = empleado2[1]
    return empleado2[0]
  
  return empleado1[0]

empleado1 = nameSueldo()
empleado2= nameSueldo()
print(f"la empleado que tiene un sueldo mayor es: {mayorSueldo(empleado1, empleado2)}")






""" def tuplas(number: int) -> tuple:
  valor = (number, number**2)
  return valor

resultado = tuplas(10)
print(resultado)
print(type(resultado))

def cargar_fecha():
    dd=int(input("Ingrese numero de dia:"))
    mm=int(input("Ingrese numero de mes:"))
    aa=int(input("Ingrese numero de año:"))
    return (dd,mm,aa)


def imprimir_fecha(fecha):
    print(fecha[0],fecha[1],fecha[2],sep="/")


# bloque principal

fecha=cargar_fecha()
imprimir_fecha(fecha)

fechatupla1=(25, 12, 2016)
print("Imprimimos la primer tupla")
print(fechatupla1)
fechalista=list(fechatupla1)
print("Imprimimos la lista que se le copio la tupla anterior")
print(fechalista)
fechalista[0]=31
print("Imprimimos la lista ya modificada")
print(fechalista)
fechatupla2=tuple(fechalista)
print("Imprimimos la segunda tupla que se le copio la lista")
print(fechatupla2) """
