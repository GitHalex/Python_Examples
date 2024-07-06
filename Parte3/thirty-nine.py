import random as r

def cargar() -> list:
  lista = [r.randint(0, 10) for _ in range(10)]
  return lista

def imprimir(lista: list) -> None:
  print(lista)

def mezclar(lista) -> list:
  return r.shuffle(lista)

lista=cargar()
print("Lista generada aleatoriamente")
imprimir(lista)
mezclar(lista)
print("La misma lista luego de mezclar")
imprimir(lista)