from persona import Persona # es mejor importar de esta manera para evitar confidir nombres entres los modulos de las clases u objetos y lo que hago es importar del archivo persona.py la clase Persona

class Usuario(Persona):
    def __init__(self, nombre="", apellido="", dni=""): 
        super().__init__(nombre, apellido, dni) # esto lo que hace es llamar al constructor de la clase persona, con super, para que la subclase puede acceder a los atributos
        self._motivo = "" # creo el atributo motivo

    # aca estoy sobreescribiendo el metodo ingresar dato, y en cada uno de los atributos esta el self.__ para acceder a ese atributo y mediante el imput darle un valor 
    def ingresar_datos(self):
        self._nombre = input("Ingrese el nombre del usuario: ")
        self._apellido = input("Ingrese el apellido del usuario: ")
        self._dni = input("Ingrese el DNI del usuario: ")
        self._motivo = input("Motivo de la consulta: ")

    # este metodo permite ver el motivo de la consulta
    def mostrar_motivo(self):
        return self._motivo
