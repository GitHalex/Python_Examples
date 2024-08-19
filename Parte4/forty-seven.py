class Persona:
  def __init__(self, nombre: str, edad: int, nacionalidad: str) -> None:

    self.nombre_completo = f"nombre => {nombre}\nedad => {edad}\nnacionalidad => {nacionalidad}"
  def hablar(self):
    print("Hola, estoy hablando un poco")


class Empleado(Persona):
  def __init__(self, nombre: str, edad: int, nacionalidad: str, trabajo: str, salario: float) -> None:
    super().__init__(nombre, edad, nacionalidad)
    self.trabajo = trabajo
    self.salario = salario

class Estudiante(Persona):
  def __init__(self, nombre: str, edad: int, nacionalidad: str, notas: float, universidad: str) -> None:
    super().__init__(nombre, edad, nacionalidad)
    self.notas = notas
    self.universidad = universidad

roberto = Empleado("Roberto", 23, "boliviano", "programador", 100.4)
roberto.hablar()
print(roberto.salario)