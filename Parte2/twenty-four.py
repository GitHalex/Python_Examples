
def cantidadVocales(palabra: str) -> int:
    print(f"Palabra: {palabra}")
    contar_vocales = 0
    for char in palabra:
        vocal = char.lower()
        if vocal in "aeiouáéíóú":
            contar_vocales += 1
    return contar_vocales

print(cantidadVocales("Alex López"))

