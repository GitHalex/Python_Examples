""" def cargar() -> None:
    lista=[input("Ingrese una palabra: ") for _ in range(3)]
    return lista

def imprimir(lista):
    print("Lista completa")
    for elemento in lista:
        if len(elemento) > 5:
            print(f"elemento con mas de 5 caracteres: {elemento}") """

""" def mayor(lista):
    may=lista[0]
    for elemento in lista:
        if elemento>may:
            may=elemento
    print("El elemento mayor de la lista es",may)            
        

def sumar_elementos(lista):
    suma=0
    for elemento in lista:
        suma=suma+elemento
    print("La suma de todos sus elementos es",suma) """


# bloque principal

""" lista=cargar()
imprimir(lista) """
""" mayor(lista)
sumar_elementos(lista)
 """




def cargar() -> list: 
    productos=[(input("ingrese el nombre del producto: "), int(input("Ingrese su precio: "))) for _ in range(3)]
    return productos

def imprimir(productosPrecios: tuple) -> None:
    print("Listado de los productos y sus precios")
    for producto, precio in productosPrecios:
        print(f"Producto: {producto} => Precio: {precio}")

def mayor_precio(productosPrecios: tuple) -> None:
    print("Procto en el rango de 10 y 15")
    for producto, precio in productosPrecios:
        if precio >= 10 and precio <= 15:
            print(f"Producto: {producto} => precio: {precio}")


# bloque principal
productoPrecio = cargar()
imprimir(productoPrecio)
mayor_precio(productoPrecio)

""" empleados=cargar()
imprimir(empleados)
mayor_sueldo(empleados)                        
sueldos_menor1000(empleados) """