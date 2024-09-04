class Persona:
  def __init__(self, nombre: str, edad: int) -> None:
    self.__nombre = nombre
    self._edad = edad
    
  @property
  def nombre(self):
    return self.__nombre
  
  @nombre.setter
  def nombre(self, new_nombre: str):
    self.__nombre = new_nombre
    
  @nombre.deleter
  def nombre(self):
    del self.__nombre
    
dalto = Persona("Lucas", 21)
nombre = dalto.nombre
print(nombre, "esto")

dalto.nombre = "Pepe"
nombre = dalto.nombre
print(nombre, "es")

del dalto.nombre
print(nombre, "ultimo")
