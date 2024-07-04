def capicua(cadena):
    indice=-1
    iguales=0
    for x in range(0,len(cadena)//2):
        if cadena[x]==cadena[indice]:
            iguales=iguales+1
        indice=indice-1
    print(cadena)
    if iguales==(len(cadena)//2):
        print("Es capicua")
    else:
        print("No es capicua")
    

# bloque principal

capicua("neuquen")
capicua("casa")

def cargarCadena(cadena: str) -> None:
    
    nuevaCadena = ""
    primero, ultimo = cadena[-1], cadena[0]
    print(primero)
    print(ultimo)
    nuevaCadena += primero
    for i in range(1, len(cadena) -1):
        nuevaCadena += cadena[i]

    nuevaCadena += ultimo

    print(nuevaCadena)
        
        
    

cargarCadena("alex")
