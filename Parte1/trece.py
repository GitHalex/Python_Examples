""" frase = input("Ingrese una frase: ")
cadena_vacia = 0
for char in frase:
    if char == " ":
        cadena_vacia += 1

print(f"La frase tiene {cadena_vacia} espacios vacios") """

frase = input("Ingrese una frase: ")
cant_vocales = 0
frase_min = frase.lower()
for i in frase_min:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        cant_vocales += 1
print(f"cantidad de vocales: {cant_vocales}")
