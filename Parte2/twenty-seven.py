""" def sueldosPersonas() -> list:
    li=[]
    for x in range(10):
        valor=int(input("Ingrese valor:"))
        li.append(valor)
    return li
def imprimirSueldos(li: list) -> None:
    print("*******************************")
    print("*   Sueldos de los empleados  *")
    print("*******************************")   
    for i in range(len(li)):
        print(f"{i+1} -> {li[i]}")
def sueldosMayoresInferiores(sueldos: list) -> None:
    cantidad = 0
    for sueldo in sueldos:
        if sueldo > 40:
            cantidad += 1
        else:
            print(f"sueldo inferior: {sueldo}")       
    print(f"la lista: {sueldos} tiene {cantidad} superiores a 40")
def promedioSueldos(listaSueldos: list) -> float:    
    suma = 0
    for sueldo in listaSueldos:
        suma += sueldo
    promedio = suma/len(listaSueldos)
    return promedio
def mostrarMenores(listaSueldos: list) -> None:
    for sueldo in listaSueldos:
        if sueldo < promedioSueldos(listaSueldos):
            print(sueldo)
# bloque principal del programa
sueldos = sueldosPersonas()
imprimirSueldos(sueldos)
print(sueldosMayoresInferiores(sueldos))
promedio = promedioSueldos(sueldos)
print(f"El promedio de los sueldos es: {promedio}")
mostrarMenores(sueldos) """

""" def nombrePrecio() -> list:

  nombreLista = []
  precioLista = []
  for i in range(5):
    nombre = input("Ingresa un nombre: ")
    nombreLista.append(nombre)
    precio = float(input("Ingrese el precio: "))
    precioLista.append(precio)
  
  return [nombreLista, precioLista]

def imprimirPrecios(listaNombre: list, listaPrecios: list) -> list:

  for i in range(len(listaNombre)):
    print(f"{listaNombre[i]} => {listaPrecios[i]}")

def preciosMayor(listaPrecios: list) -> list:

  nuevoPrecio = []
  subePrecio = int(input("Ingrese cuanto va a subir cada articulo: "))
  for i in range(len(listaPrecios)):
    nuevoPrecio.append(listaPrecios[i] + subePrecio)

  return nuevoPrecio

def precioImporte(listaPrecios: list) -> None:

  importe = int(input("Ingrese un importe: "))
  for precio in listaPrecios:
    if precio <= importe:
      print(precio)


nombres, precios = nombrePrecio()
print("Impresion de Articulos y Precios")
imprimirPrecios(nombres, precios)
print("Impresion de Articulos con subida de precio")
preciosAumentados = preciosMayor(precios)
imprimirPrecios(nombres, preciosAumentados)
print("Precios con importe ")
precioImporte(precios) """


def cargarLista() -> list:

  listaTen = []
  for i in range(10):
    numero = int(input("Ingrese un numero positivos o negativos: "))
    listaTen.append(numero)

  return listaTen

def positivoNegativo(listaNum: list) -> list:

  positivos = [i for i in listaNum if i >= 0]
  negativos = [j for j in listaNum if j < 0]

  return [positivos, negativos]


listaNumero = cargarLista()
numerosPositivos, numerosNegativos = positivoNegativo(listaNumero)

print("Numeros Positivos")
for positivo in numerosPositivos:
  print(positivo)

print("Numeros Negativos")
for negativo in numerosNegativos:
  print(negativo)





""" def carga_lista():
    li=[]
    for x in range(5):
        valor=int(input("Ingrese valor:"))
        li.append(valor)
    return li


def retornar_mayormenor(li):
    ma=li[0]
    me=li[0]
    for x in range(1,len(li)):
        if li[x]>ma:
            ma=li[x]
        else:
            if li[x]<me:
                me=li[x]
    return [ma,me]                


# bloque principal del programa

lista=carga_lista()
rango=retornar_mayormenor(lista)
print("Mayor elemento de la lista:",rango[0])
print("Menor elemento de la lista:",rango[1]) """


""" def cargar_datos():
    nom=[]
    ed=[]
    for x in range(5):
        v1=input("Ingrese el nombre de la persona:")
        nom.append(v1)
        v2=int(input("Ingrese la edad:"))
        ed.append(v2)
    return [nom,ed]


def mayores_edad(nom,ed):
    print("Nombres de personas mayores de edad")
    for x in range(len(nom)):
        if ed[x]>=18:
            print(nom[x])


def promedio_edades(ed):
    suma=0
    for x in range(len(ed)):
        suma=suma+ed[x]
    promedio=suma//5
    print("Edad promedio de las personas:",promedio)
    

# bloque principal

nombres,edades=cargar_datos()
mayores_edad(nombres,edades)
promedio_edades(edades) """