
def cantidadVocales(palabra: str) -> int:
    print(f"Palabra: {palabra}")
    contar_vocales = 0
    for char in palabra:
        vocal = char.lower()
        if vocal in "aeiouáéíóú":
            contar_vocales += 1
    return contar_vocales

print(cantidadVocales("Alex López"))

def ordenados(lista: list) -> list:

    ordenar = sorted(lista)
    return ordenar

def cargarNumeros() -> list:
    listaNumeros = []
    for i in range(3):
        numero = int(input("Ingrese un numero"))
        listaNumeros.append(numero)

    return ordenados(listaNumeros)

print(cargarNumeros())
