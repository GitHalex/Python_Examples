def listaNumeros() -> list:
  listaEnteros = [int(input("Ingrese un numero: ")) for _ in range(5)]
  return listaEnteros

lista = listaNumeros()
