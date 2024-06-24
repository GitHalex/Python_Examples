
def productoTen(numero: int, multiplicador: int=10) -> str:
    imprimir = ""
    for i in range(1, multiplicador + 1):
        imprimir += f"{i} x {numero} = {i*numero}\n"

    return imprimir

print(productoTen(2))