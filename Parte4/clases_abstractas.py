from abc import ABC, abstractclassmethod

class Persona(ABC):
  @abstractclassmethod
  def __init__(self, nombre, edad, sexo, trabajo) -> None:
    self.nombre = nombre
    self.edad = edad
    self.sexo = sexo
    self.trabajo = trabajo
    
  @abstractclassmethod
  def trabajar(self):
    pass
  
  def presentarse(self):
    print(f"Hola me llamo: {self.nombre} y tengo {self.edad} años")
    
    