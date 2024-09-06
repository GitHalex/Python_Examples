class Cliente:
  
  suspendidos = []

  def __init__(self, codigo: int, nombre: str) -> None:
    self.codigo = codigo
    self.nombre = nombre
  
  def imprimir(self):
    print(f"Codigo: {self.codigo}")
    print(f"Nombre: {self.nombre}")

  def esta_suspendido(self):
    if self.codigo in Cliente.suspendidos:
      print(f"{self.nombre} => ESta suspendido")
    else:
      print("No esta suspendido")
    
    print("______________________________")

  def suspender(self):
    Cliente.suspendidos.append(self.codigo)
    

cliente1 = Cliente(1, "Juan")
cliente2 = Cliente(2, "Ana")
cliente3 = Cliente(3, "Diego")
cliente4 = Cliente(4, "Pedro")

cliente3.suspender()
cliente3.esta_suspendido()

cliente1.imprimir()
cliente2.imprimir()
cliente3.imprimir()
cliente4.imprimir()

print(Cliente.suspendidos)