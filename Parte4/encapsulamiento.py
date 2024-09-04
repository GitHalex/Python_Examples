class Persona:
  def __init__(self, nombre: str, edad: int) -> None:
    self.__nombre = nombre
    self.__edad = edad
  
  def get_nombre(self):
    return self.__nombre
  
  def set_nombre(self, new_nombre: str):
    self.__nombre = new_nombre
  
  
persona1 = Persona("Alex", 23)
nombre = persona1.get_nombre()
print(nombre)
  
  
  