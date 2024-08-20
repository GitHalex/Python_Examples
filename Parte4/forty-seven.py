class Persona:
  def __init__(self, nombre: str, edad: int) -> None:
    self.nombre = nombre
    self.edad = edad
    self.nombre_completo = f"nombre => {nombre}\nedad => {edad}"

  @classmethod
  def entrada_usuario(cls):
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese su edad: "))
    return cls(nombre, edad)
  
  def hablar(self):
    print("Hola, estoy hablando un poco")
  
  def imprimir(self):
    print(f"Nombre => {self.nombre} ")
    print(f"Edad => {self.edad}")


class Empleado(Persona):
  def __init__(self, nombre: str, edad: int, trabajo: str, salario: float) -> None:
    super().__init__(nombre, edad)
    self.trabajo = trabajo
    self.salario = salario

  @classmethod
  def entrada_trabajo_salario(cls):
    trabajo = input("Cual es tu puesto de trabajo")
    salario = int(input("Cual es tu sueldo: "))
    return cls(trabajo, salario)
  
  def imprimir(self):
    super().imprimir()
    print(f"Sueldo => {self.salario}")

  def paga_impuestos(self):
    if self.salario > 1000:
      print("El empleado debe pagar impuestos")
    else:
      print("No paga impuestos")


persona1 = Persona.entrada_usuario()
persona1.imprimir()
print("-----------------------------------------------")
empleado1 = Empleado.entrada_trabajo_salario()
empleado1.imprimir()
empleado1.paga_impuestos()