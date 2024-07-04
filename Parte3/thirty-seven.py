def cargarLista() -> list:
    listaNumeros = [int(input("Ingrese un numero: ")) for _ in range(10)]
    return listaNumeros

def primerMitad(listaNum: list) -> list:
    mitad = len(listaNum) // 2
    return listaNum[:mitad]

lista = cargarLista()
listaMitad = primerMitad(lista)
print(f"lista Mitad primera: {listaMitad}")
print(lista)



""" lista1=[0,1,2,3,4,5,6]
lista2=lista1[2:5]
print(lista2) # 2,3,4
lista3=lista1[1:3]
print(lista3) # 1,2
lista4=lista1[:3]
print(lista4) # 0,1,2
lista5=lista1[2:]
print(lista5) # 2,3,4,5,6 """

""" def meses_faltantes(numeromes):
    meses=('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
    return meses[numeromes:]


# bloque principal

print("Imprimir los nombres de meses que faltan hasta fin de año")
numeromes=int(input("Ingrese el numero de mes:"))
mesesfalta=meses_faltantes(numeromes)
print(mesesfalta)

def primeros_tres(cadena):
    return cadena[:3];


# bloque principal

meses=('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
for x in meses:
    print(primeros_tres(x)) """