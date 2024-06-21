def multiplicar(listaNum: int, numero: int) -> list:
    
    resultado = []

    for i in listaNum:
        resultado.append(i*numero)

    return resultado


listaNum=[3, 7, 8, 10, 2]
print(multiplicar(listaNum,3))


def mascaracteres(palabras: list) -> str:
    
    palabrasLarga = ""

    for palabra in palabras:
        if len(palabrasLarga) < len(palabra):
            palabrasLarga = palabra

    return palabrasLarga

palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print("Palabra con mas caracteres:",mascaracteres(palabras))


def sumarizar(lista):
    suma=0
    for x in range(len(lista)):
        suma=suma+lista[x]
    return suma


def mayor(lista):
    may=lista[0]
    for x in range(1,len(lista)):
        if lista[x]>may:
            may=lista[x]
    return may


def menor(lista):
    men=lista[0]
    for x in range(1,len(lista)):
        if lista[x]<men:
            men=lista[x]
    return men
    

# bloque principal del programa

""" listavalores=[10, 56, 23, 120, 94]
print("La lista completa es")
print(listavalores)
print("La suma de todos su elementos es", sumarizar(listavalores))
print("El mayor valor de la lista es", mayor(listavalores))
print("El menor valor de la lista es", menor(listavalores))


def mayormenor(lista):
    may=lista[0]
    men=lista[0]
    for x in range(1,len(lista)):
        if lista[x]>may:
            may=lista[x]
        else:
            if lista[x]<men:
                men=lista[x]
    print("El valor mayor de la lista es", may)
    print("El valor menor de la lista es", men)          

                
# bloque principal

lista=[]
for x in range(5):
    valor=int(input("Ingrese valor:"))
    lista.append(valor)
mayormenor(lista) """