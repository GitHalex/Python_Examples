def ciudadanos() -> dict:
    segip = {}
    for i in range(1, 5):
        ci = str(i) + str(int(input("Ingrese cedula de identidad: ")))
        nombre = input("Ingrese su nombre: ")
        segip[ci] = nombre
        
    return segip

def imprimir(dictSegip: dict) -> None:
    print("LISTADO COMPLETO DEL DICCIONARIO")
    for ci in dictSegip:
        print(f"CI: {ci} => Nombre: {dictSegip[ci]}")
    
def consultaNombre(dictSegip: dict) -> None:
    print("CONSULTA EL NOMBRE: ")
    ci = int(input("Ingrese el ci:"))
    if ci in dictSegip:
        print(f"CI:{ci} Nombre:{dictSegip[ci]}")
    else:
        print(f"CI:{ci} no existe en el dictionario\n{dictSegip}")

segipDicccionario = ciudadanos()
imprimir(segipDicccionario)
consultaNombre(segipDicccionario)
        
        

