class TanqueDeCombustible:
    def __init__(self) -> None:
        self.combustible = 100

    def agregar_combustible(self, cantidad):
        self.combustible += cantidad

    def obtener_combustible(self):
        return self.combustible

    def usar_combustible(self, cantidad):
        self.combustible -= cantidad


class Motor:
    def __init__(self, tanque: TanqueDeCombustible) -> None:
        self.tanque = tanque

    def puede_mover(self, distancia):
        # Chequea si hay suficiente combustible para moverse
        return self.tanque.obtener_combustible() >= distancia / 2

    def consumir_combustible(self, distancia):
        # Usa el combustible según la distancia
        self.tanque.usar_combustible(distancia / 2)


class Auto:
    def __init__(self, motor: Motor) -> None:
        self.posicion = 0
        self.motor = motor

    def mover(self, distancia):
        if self.motor.puede_mover(distancia):
            self.posicion += distancia
            self.motor.consumir_combustible(distancia)
            print("Has movido el auto exitosamente")
        else:
            print("No hay suficiente combustible")

    def obtener_posicion(self):
        return self.posicion


# Uso de las clases
tanque = TanqueDeCombustible()
motor = Motor(tanque)
autito = Auto(motor)
print(autito.obtener_posicion())
autito.mover(10)
print(autito.obtener_posicion())
