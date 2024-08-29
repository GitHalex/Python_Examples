class Pato:
    def hablar(self):
        return "cuac cuac"

class Perro:
    def hablar(self):
        return "guau guau"

def hacer_hablar(animal):
    print(animal.hablar())

pato = Pato()
perro = Perro()

hacer_hablar(pato)  # Imprime "cuac cuac"
hacer_hablar(perro)  # Imprime "guau guau"


class Animal:
    def hablar(self):
        print("El animal hace un sonido")

class Perro(Animal):
    def hablar(self):
        print("Guau guau")

class Gato(Animal):
    def hablar(self):
        print("Miau miau")

def hablar_estaticamente(animal: Animal):
    # Enlace "estático" porque se espera que siempre sea de tipo Animal
    animal.hablar()

perro = Perro()
gato = Gato()

hablar_estaticamente(perro)  # Guau guau
hablar_estaticamente(gato)   # Miau miau





def hablar_dinamicamente(animal):
    # No especificamos el tipo exacto de animal; Python determinará
    # en tiempo de ejecución qué método invocar
    animal.hablar()

perro = Perro()
gato = Gato()

hablar_dinamicamente(perro)  # Guau guau
hablar_dinamicamente(gato)   # Miau miau


class Vehiculo:
    def arrancar(self):
        print("El vehículo arranca")

class Coche(Vehiculo):
    def arrancar(self):
        print("El coche arranca")

def iniciar_vehiculo(vehiculo: Vehiculo):
    # Tipo declarado: Vehiculo
    vehiculo.arrancar()

mi_vehiculo = Coche()  # Tipo real: Coche
iniciar_vehiculo(mi_vehiculo)  # Imprime "El coche arranca"
