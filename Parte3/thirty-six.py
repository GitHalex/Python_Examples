""" def cargar():
    lista=[]
    continua="s"
    while continua=="s":
        valor=int(input("Ingrese un valor:"))
        lista.append(valor)
        continua=input("Agrega otro elemento a la lista[s/n]:")
    return lista

def fijar_cero(li):
    for x in range(len(li)):
        if li[x]<10:
            li[x]=0

def imprimir(lista):
    for elemento in lista:
        print(elemento,"-",sep="",end="")
    print("")

# bloque principal
lista=cargar()
print("Lista antes de modificar")
imprimir(lista)
fijar_cero(lista)
print("Lista despues de modificar")
imprimir(lista)

def cargar():
    nombres=[]
    for x in range(5):
        nom=input("Ingrese nombre:")
        nombres.append(nom)
    return nombres

def ordenar(nombres):
    for k in range(4):
        for x in range(4):
            if nombres[x]>nombres[x+1]:
                aux=nombres[x]
                nombres[x]=nombres[x+1]
                nombres[x+1]=aux

def imprimir(nombres):
    for x in range(len(nombres)):
        print(nombres[x]," ",end="")

# bloque principal
nombres=cargar()
ordenar(nombres)
imprimir(nombres) """

def cargarDatos() -> dict:
    datosEmpleados = {}
    
    for i in range(3):
        numero = int(input("Ingrese un numero: "))
        nombre = input("Ingrese el nombre de un empleado: ")
        profesion = input("Ingrese su profesion: ")
        sueldo = float(input("Ingrese su sueldo: "))
        datosEmpleados[numero] = [nombre, profesion, sueldo]
      
    return datosEmpleados

def modificarSueldo(diccionario: dict) -> None:
    
    numClave = int(input("Ingrese el numero para modificar sueldo: "))
    
    if numClave in diccionario:
      sueldoModificado = float(input("Ingrese un nuevo sueldo: "))
      diccionario[numClave][2] = sueldoModificado
    else:
      print(f"{numClave} numero clave no existe en el diccionario: {diccionario}")

diccionarioEmpleados = cargarDatos()
print(diccionarioEmpleados)
modificarSueldo(diccionarioEmpleados)
print(diccionarioEmpleados)


""" def cargar():
    contactos={}
    continua="s"
    while continua=="s":
        nombre=input("Ingrese el nombre del contacto:")
        telefono=input("Ingrese el numero de telefono:")
        contactos[nombre]=telefono
        continua=input("Ingresa otro contacto[s/n]?:")
    return contactos


def modificar_telefono(contactos):
    nombre=input("Ingrese el nombre de contacto a modificar el telefono:")
    if nombre in contactos:
        telefono=input("Ingrese el nuevo numero telefonico")
        contactos[nombre]=telefono
    else:
        print("No existe un contacto con el nombre ingresado")


def imprimir(contactos):
    print("Listado de todos los contactos")
    for nombre in contactos:
        print(nombre,contactos[nombre])


# bloque principal

contactos=cargar()
modificar_telefono(contactos)
imprimir(contactos) """
