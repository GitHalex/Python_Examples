class Cliente:
    def __init__(self, nombre: str) -> None:
        """Inicializa un cliente con su nombre y un monto inicial de 0."""
        self.nombre = nombre
        self.monto = 0

    def depositar(self, monto: float) -> None:
        """Deposita un monto en la cuenta del cliente."""
        if monto > 0:
            self.monto += monto
        else:
            print(f"El monto a depositar debe ser positivo. Monto ingresado: {monto}")

    def extraer(self, monto: float) -> None:
        """Extrae un monto de la cuenta del cliente si es posible."""
        if 0 < monto <= self.monto:
            self.monto -= monto
        else:
            print(f"El monto a extraer es inválido. Monto ingresado: {monto}, Saldo disponible: {self.monto}")

    def retornar_monto(self) -> float:
        """Devuelve el monto actual del cliente."""
        return self.monto

    def imprimir(self) -> None:
        """Imprime el nombre del cliente y su monto actual."""
        print(f"{self.nombre} tiene depositado la suma de {self.monto}")

class Banco:
    def __init__(self) -> None:
        """Inicializa el banco con tres clientes predeterminados."""
        self.clientes = [
            Cliente("Juan"),
            Cliente("Ana"),
            Cliente("Diego")
        ]
    def operar(self) -> None:
        """Realiza operaciones de depósito y extracción para los clientes."""
        self.clientes[0].depositar(100)
        self.clientes[1].depositar(150)
        self.clientes[2].depositar(200)
        self.clientes[2].extraer(150)
        self.clientes[0].depositar(200)

    def depositos_totales(self) -> None:
        """Calcula y muestra el monto total depositado en el banco."""
        total = sum(cliente.retornar_monto() for cliente in self.clientes)
        print(f"El total de dinero del banco es: {total}")
        for cliente in self.clientes:
            cliente.imprimir()

""" if __name__ == "__main__":
    banco1 = Banco()
    banco1.operar()
    banco1.depositos_totales() """


from random import random, randint

class Dado:

  def tirar(self):
      self.valor = randint(1, 6)

  def imprimir(self):
      print(f"Valor del dado: {self.valor}")

  def retornar_valor(self):
      return self.valor
  
class JuegoDeDados: 
  
  def __init__(self) -> None:
      self.dado1 = Dado()
      self.dado2 = Dado()
      self.dado3 = Dado()

  def jugar(self):
      self.dado1.tirar()
      self.dado1.imprimir()
      self.dado2.tirar()
      self.dado3.tirar()
      self.dado3.imprimir()
      if self.dado1.retornar_valor()==self.dado2.retornar_valor() and self.dado1.retornar_valor()==self.dado3.retornar_valor():
          print("Gano")
      else:
          print("Perdio")


""" juego_dados = JuegoDeDados()
juego_dados.jugar() """

class Socio:
    
    def __init__(self, nombre: str, antiguedad: str) -> None:
        self.nombre = nombre
        self.antiguedad = antiguedad

    @classmethod
    def entrada_usuario(cls):
        nombre = input("Ingrese el nombre del socio: ")
        antiguedad = input("Ingrese el mes y año ejemplo 'ENERO 2024'")
        return cls(nombre, antiguedad)
    
    def mostrar(self):
        print(f"{self.nombre} => {self.antiguedad}")

class Club:
    
    def __init__(self) -> None:
        self.socios = [
            Socio.entrada_usuario(),
            Socio.entrada_usuario()
        ]

    def imprimir(self):
        self.socios[0].mostrar()


if __name__ == "__main__":
    socio = Club()
    socio.imprimir()
