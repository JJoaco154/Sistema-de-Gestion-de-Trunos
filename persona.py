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