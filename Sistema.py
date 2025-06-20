from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, apellido, dni): # el __init__ lo uso como constructor y me permite inicializar los atributos de la clase
        self._nombre = nombre # con el __ estoy encapsulando los atributos haciendolos privados
        self._apellido = apellido
        self._dni = dni

    # metodos para acceder a los atributos encapsulados (get)
    def mostrar_nombre(self):
        return self._nombre

    def mostrar_apellido(self):
        return self._apellido

    def mostrar_dni(self):
        return self._dni
    
    # metodo abstracto para que las clases hijas lo puedan sobreescribir
    @abstractmethod
    def ingresar_datos(self):
        pass


# aca creo la clase usuario hereda todos los atibutos y metodos de la clase persona
class Usuario(Persona):
    def __init__(self, nombre="", apellido="", dni=""):
        super().__init__(nombre, apellido, dni) # esto lo que hace es llamar al constructor de la clase persona, con super, para que la subclase puede acceder a los atributos
        
    # aca estoy sobreescribiendo el metodo ingresar dato, y en cada uno de los atributos esta el self.__ para acceder a ese atributo y mediante el imput darle un valor 
    def ingresar_datos(self):
        self._nombre = input("Ingrese el nombre del usuario: ")
        self._apellido = input("Ingrese el apellido del usuario: ")
        self._dni = input("Ingrese el DNI del usuario: ")
        self.motivo = input("Motivo de la consulta: ")

    # este metodo permite ver el motivo de la consulta
    def mostrar_motivo(self):
        return self.motivo


class Profesional(Persona):
    def __init__(self, nombre="", apellido="", dni=""):
        super().__init__(nombre, apellido, dni) # esto funciona igual que en la clase usuario

    # esto tambien funciona igual que la clase usuario
    def ingresar_datos(self):
        self._nombre = input("Ingrese el nombre del profesional: ")
        self._apellido = input("Ingrese el apellido del profesional: ")
        self._dni = input("Ingrese el DNI del profesional: ")
        self.especialidad = input("Ingrese la especialidad del profesional: ")

    # esto permite retornar el la esoecialidad del profacional
    def mostrar_especialidad(self):
        return self.especialidad

class datos_visita():
    def ingresar_dia(self):
        self.dia = input("Ingrese el dia de la visita: ")

    def mostrar_dia(self):
        return self.dia

    def ingresar_hora(self):
        self.hora = input("Ingrese la hora de la visita: ")
    
    def mostrar_hora(self):
        return self.hora
    
    def ingresar_monto(self):
        self.monto = input("Ingrese el monto a pagar: ")
    
    def mostrar_monto(self):
        return self.monto


# esta es la clase la cual muestra el detalle de la visita y tiene una relacion de agragacion porque tiene 2 objetos dentro de si Usuario y Profecional creados previamente por fuera de la clase
class detalle_visita(Usuario, Profesional):
    # aca es donde recibe los dos objetos y los alamcena internamente para despues trabajar con ellos
    def __init__(self, usuario, profesional, datos_visita):
        self.usuario = usuario
        self.profesional = profesional
        self.datos_visita = datos_visita
    
    # este metodo simplemente muestra cada uno de los objetos, formateando las cadenas de texto con f
    def mostrar_detalle(self):
        print("\n--- Detalle de la visita ---")
        print(f"Usuario: {self.usuario.mostrar_nombre()} {self.usuario.mostrar_apellido()} - DNI: {self.usuario.mostrar_dni()}")
        print(f"Profesional: {self.profesional.mostrar_nombre()} {self.profesional.mostrar_apellido()} - DNI: {self.profesional.mostrar_dni()} - Especialidad: {self.profesional.mostrar_especialidad()}")
        print(f"Motivo de la consulta: {self.usuario.mostrar_motivo()}")
        print(f"Dia del turno: {self.datos_visita.mostrar_dia()}, a la hora: {self.datos_visita.mostrar_hora()}, monto a pagar: {self.datos_visita.mostrar_monto()}")



