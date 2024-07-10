""" class Alumno:

    def inicializar(self,nombre: str,nota: int):
        self.nombre=nombre
        self.nota=nota

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Nota:",self.nota)

    def mostrar_estado(self):
        if self.nota>=4:
            print("Regular")
        else:
            print("Libre")


# bloque principal

alumno1=Alumno()
alumno1.inicializar("diego",2)
alumno1.imprimir()
alumno1.mostrar_estado()

alumno2=Alumno()
alumno2.inicializar("ana",10)
alumno2.imprimir()
alumno2.mostrar_estado() """

""" class Persona:
    def inicializar(self, nombre: str, edad: int): 
        self.name = nombre
        self.age = edad

    def mostrar(self):
        print(f"Nombre: {self.name}")
        print(f"Edad: {self.age}")

    def mayorEdad(self):
        if self.age > 18:
            print("Mayor de edad")
        else:
            print("Menor de edad")

persona1 = Persona()
persona1.inicializar("Alex", 2)
persona1.mostrar()
persona1.mayorEdad() """


class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def lado_mayor(self):
        return max(self.lado1, self.lado2, self.lado3)

    def es_equilatero(self):
        return self.lado1 == self.lado2 == self.lado3

    def __str__(self):
        equilatero = "es equilátero" if self.es_equilatero() else "no es equilátero"
        return f"Triángulo con lados {self.lado1}, {self.lado2}, {self.lado3}. Lado mayor: {self.lado_mayor()}. El triángulo {equilatero}."

# Ejemplo de uso
if __name__ == "__main__":
    # Cargar los lados del triángulo
    lado1 = float(input("Ingrese el primer lado del triángulo: "))
    lado2 = float(input("Ingrese el segundo lado del triángulo: "))
    lado3 = float(input("Ingrese el tercer lado del triángulo: "))

    # Crear una instancia de la clase Triangulo
    triangulo = Triangulo(lado1, lado2, lado3)

    # Imprimir el valor del lado mayor
    print(f"El lado mayor del triángulo es: {triangulo.lado_mayor()}")

    # Mostrar si el triángulo es equilátero o no
    if triangulo.es_equilatero():
        print("El triángulo es equilátero.")
    else:
        print("El triángulo no es equilátero.")
