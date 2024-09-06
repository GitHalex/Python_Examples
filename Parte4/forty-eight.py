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

print(Cliente.suspendidos)

print("############################")

class Jugador:
  
  # Variable de clase que indica los minutos que faltan para el fin del juego
  tiempo_restante = 30

  
  def __init__(self, nombre: str, puntaje: int) -> None:
    self.nombre = nombre
    self.puntaje = puntaje
    
  def imprimir(self) -> None:
    # imprime los detalles del jugador
    print(f"Nombre => {self.nombre}")
    print(f"Puntaje => {self.puntaje}")
    
  @classmethod
  def pasar_tiempo(cls) -> None:
    # Reduce el tiempo restante del juego
    if cls.tiempo_restante > 0:
      cls.tiempo_restante -= 1
      print(f"Tiempo restante: {cls.tiempo_restante} minutos")
    else:
      print("El juego ha temrinado")

#Bloque principal
jugador1 = Jugador("Carlos", 10)
jugador2 = Jugador("Ana", 20)

# Imprimir información de los jugadores
jugador1.imprimir()
jugador2.imprimir()

# Reducir el tiempo hasta que llegue a cero
while Jugador.tiempo_restante > 0:
    Jugador.pasar_tiempo()
    # Imprimir información de los jugadores
    jugador1.imprimir()
    jugador2.imprimir()

      
    
 
