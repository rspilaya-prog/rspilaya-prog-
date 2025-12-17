class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.__edad = edad  # atributo privado

    def mostrar_edad(self):
        return self.__edad

persona = Persona("Ana", 20)
print("Edad:", persona.mostrar_edad())

