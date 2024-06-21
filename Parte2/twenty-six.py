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


def producto(listaNumeros: list) -> int:
    
    producto = 1

    for numero in listaNumeros:
        producto *= numero

    
    return producto
    


listaEnteros = []

for j in range(5):
    numero = int(input("Ingrese un numero: "))
    listaEnteros.append(numero)

print(f"el producto de la lista: {listaEnteros} es: {producto(listaEnteros)}")


