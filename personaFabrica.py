from usuario import Usuario
from profesional import Profesional

class PersonaFabrica:
    def crear_persona(self, tipo):
        tipo = tipo.lower()
        if tipo == "usuario":
            return Usuario()
        elif tipo == "profesional":
            return Profesional()
        else:
            raise ValueError(f"Tipo de persona desconocido: {tipo}")
