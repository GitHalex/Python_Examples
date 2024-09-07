class Familia:
  
  def __init__(self, padre:str, madre: str, hijos: str=[]) -> None:
    self.padre = padre
    self.madre = madre
    self.hijos = hijos
    
  def __str__(self) -> str:
    cadena = self.padre+", "+self.madre
    for hi in self.hijos:
      cadena = cadena + ", " +hi
      
    return cadena
  
#bloque principal
familia1 = Familia("Pablo", "Ana", ["Pepe", "Julio"])
print(familia1)

class Jugador:
  def __init__(self, nombre: str, puntaje: int) -> None:
    self.nombre = nombre
    self.puntaje = puntaje
  
  def __str__(self) -> str:
    if self.puntaje < 100:
      return f"{self.nombre} con {self.puntaje} es: principiante "
    else:
      return f"{self.nombre} con {self.puntaje} es: experto"
    
  
jugador1 = Jugador("Cris", 200)
print(jugador1)
      
jugador2 = Jugador("Messi", 90)
print(jugador2)