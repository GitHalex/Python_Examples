class Empleado:

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
cuadrado1.area()