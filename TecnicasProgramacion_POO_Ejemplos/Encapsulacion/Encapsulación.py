class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("El animal hace un sonido")

class Perro(Animal):
    def hablar(self):
        print(self.nombre, "dice: Guau")

perro = Perro("Firulais")
perro.hablar()
