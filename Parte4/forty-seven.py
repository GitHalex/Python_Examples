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
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese su edad: "))
    trabajo = input("Cual es tu puesto de trabajo")
    salario = int(input("Cual es tu sueldo: "))
    return cls(nombre, edad, trabajo, salario)
  
  def imprimir(self):
    super().imprimir()
    print(f"Sueldo => {self.salario}")

  def paga_impuestos(self):
    if self.salario > 1000:
      print("El empleado debe pagar impuestos")
    else:
      print("No paga impuestos")

class Artista:
  def __init__(self, habilidad: str) -> None:
    self.habilidad = habilidad

  def mostrar_habilidad(self):
    print(f"Mi habilidad es: {self.habilidad}")

class EmpleadoArtista(Persona, Artista):
  def __init__(self, nombre: str, edad: int, habilidad: str, trabajo: str, salario: float) -> None:
    Persona.__init__(self, nombre, edad)
    Artista.__init__(self, habilidad)
    self.salario = salario
    self.trabajo = trabajo


  @classmethod
  def entrada_empleado_artista(cls):
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese su edad: "))
    trabajo = input("Cual es tu puesto de trabajo: ")
    salario = int(input("Cual es tu sueldo: "))
    habilidad = input("Ingrese su habilidad: ")
    return cls(nombre, edad, habilidad, trabajo, salario)


  def presentarse(self):
    return f"{super().mostrar_habilidad()}"


""" persona1 = Persona.entrada_usuario()
persona1.imprimir()
print("-----------------------------------------------")
empleado1 = Empleado.entrada_trabajo_salario()
empleado1.imprimir()
empleado1.paga_impuestos() """

""" roberto = EmpleadoArtista.entrada_empleado_artista()
roberto.presentarse()

herenciaHeredada = issubclass(EmpleadoArtista, Artista)
print(herenciaHeredada)

instacia = isinstance(roberto, EmpleadoArtista)
print(instacia) """



# Clase Base
class Cuenta:
    def __init__(self, nombre: str, monto: int) -> None:
        self.nombre = nombre
        self.monto = monto

    def mostrarNombre(self) -> str:
        return self.nombre

    def montoActual(self) -> int:
        return self.monto

    def mostrar_informacion(self):
        print(f"Titular: {self.nombre}, Monto actual: {self.monto}")

# Subclase PlazoFijo
class PlazoFijo(Cuenta):
    def __init__(self, nombre: str, monto: int, dias: int, tasaInteres: float) -> None:
        super().__init__(nombre, monto)  # Se llama al constructor de la clase base correctamente
        self.dias = dias
        self.tasaInteres = tasaInteres

    def calcular_intereses(self) -> float:
        # Calcula los intereses según la tasa y el plazo
        intereses = self.monto * (self.tasaInteres / 100) * (self.dias / 365)
        print(f"Intereses generados: {intereses}")
        return intereses

    def mostrar_informacion(self):
        super().mostrar_informacion()  # Muestra información básica
        print(f"Días: {self.dias}, Tasa de interés: {self.tasaInteres}%")

# Subclase CajaAhorro
class CajaAhorro(Cuenta):
    def __init__(self, nombre: str, monto: int) -> None:
        super().__init__(nombre, monto)  # Se llama al constructor de la clase base correctamente

    def mostrar_informacion(self):
        super().mostrar_informacion()  # Muestra información básica
        print("Esta cuenta no genera intereses.")

# Bloque Principal del Programa
caja_ahorro = CajaAhorro("Juan Pérez", 5000)
plazo_fijo = PlazoFijo("Ana Gómez", 10000, 30, 5)

# Muestra la información de las cuentas
caja_ahorro.mostrar_informacion()
plazo_fijo.mostrar_informacion()
plazo_fijo.calcular_intereses()



