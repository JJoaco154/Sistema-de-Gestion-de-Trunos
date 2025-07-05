from persona import Persona

class Profesional(Persona):
    def __init__(self, nombre="", apellido="", dni=""):
        super().__init__(nombre, apellido, dni) # esto funciona igual que en la clase usuario
        self._especialidad = "" # creo el atributo especialidad

    # esto tambien funciona igual que la clase usuario
    def ingresar_datos(self):
        self._nombre = input("Ingrese el nombre del profesional: ")
        self._apellido = input("Ingrese el apellido del profesional: ")
        self._dni = input("Ingrese el DNI del profesional: ")
        self._especialidad = input("Ingrese la especialidad del profesional: ")

    # esto permite retornar el la esoecialidad del profacional
    def mostrar_especialidad(self):
        return self._especialidad

