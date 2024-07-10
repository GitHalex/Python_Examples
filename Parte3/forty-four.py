""" class Empleado:

    def __init__(self):
        self.nombre=input("Ingrese el nombre del empleado:")
        self.sueldo=float(input("Ingrese el sueldo:"))

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Sueldo:",self.sueldo)

    def paga_impuestos(self):
        if self.sueldo>3000:
            print("Debe pagar impuestos")
        else:
            print("No paga impuestos")


# bloque principal

empleado1=Empleado()
empleado1.imprimir()
empleado1.paga_impuestos()


class Punto:

    def __init__(self,x: int,y: int):
        self.x=x
        self.y=y

    def imprimir(self):
        print("Coordenada del punto")
        print("(",self.x,",",self.y,")")

    def imprimir_cuadrante(self):
        if self.x>0 and self.y>0:
            print("Primer cuadrange")
        else:
            if self.x<0 and self.y>0:
                print("Segundo cuadrante")
            else:
                if self.x<0 and self.y<0:
                    print("Tercer cuadrante")
                else:
                    if self.x>0 and self.y<0:
                        print("Cuarto cuadrante")


# bloque principal

punto1=Punto(10,-2)
punto1.imprimir()
punto1.imprimir_cuadrante()

class Cuadrado:
    def __init__(self, numero: int) -> None:
        self.lado = numero

    def perimetro(self):
        perimetro = self.lado + self.lado + self.lado + self.lado
        print(perimetro)
    
    def area(self):
        areaCuadrado = self.lado * self.lado
        print(areaCuadrado)

cuadrado1 = Cuadrado(4)
cuadrado1.perimetro()
cuadrado1.area() """


class Operaciones:
    def __init__(self, primer_numero: int, segundo_numero: int) -> None:
        self.primer_numero = primer_numero
        self.segundo_numero = segundo_numero

    @classmethod
    def desde_entrada_del_usuario(cls):
        primer_numero = int(input("Ingrese el primer número: "))
        segundo_numero = int(input("Ingrese el segundo número: "))
        return cls(primer_numero, segundo_numero)

    def sumar(self) -> int:
        return self.primer_numero + self.segundo_numero

    def restar(self) -> int:
        return abs(self.primer_numero - self.segundo_numero)

    def multiplicar(self) -> int:
        return self.primer_numero * self.segundo_numero

    def dividir(self) -> float:
        if self.segundo_numero == 0:
            raise ValueError("División por cero no permitida")
        return self.primer_numero / self.segundo_numero


# Ejemplo de uso
if __name__ == "__main__":
    operacion1 = Operaciones.desde_entrada_del_usuario()
    print(f"Suma: {operacion1.sumar()}")
    print(f"Resta: {operacion1.restar()}")
    print(f"Multiplicación: {operacion1.multiplicar()}")
    try:
        print(f"División: {operacion1.dividir()}")
    except ValueError as e:
        print(e)
