
def cargar():
    lista=[]
    for x in range(5):
        valor=int(input("Ingrese valor:"))
        lista.append(valor)
    return lista


def imprimir_mayor(lista):
    may=lista[0]
    #si modificamos el rango para considerar posibeles errores esta seria la mejor opcion
    for x in range(1, len(lista)):
        if lista[x]>may:
            may=lista[x]
    print("Mayor de la lista",may)


def imprimir_suma(lista):
    suma=0
    for elemento in lista:
        suma=suma+elemento
    print("Suma de todos sus elementos",suma)

print("Me gusta ser un modulo")

if __name__ == "__main__":
    print("Prefiero ser un modulo pero puedo hacer alugar cosas pero puedo hacer algunas pruebas para usted")
    listaPrueba = cargar()
    imprimir_suma(listaPrueba)
    imprimir_mayor(listaPrueba)