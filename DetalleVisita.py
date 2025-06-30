import usuario, profesional, DatosVisita # importo las librerias

# esta es la clase la cual muestra el detalle de la visita y tiene una relacion de agragacion porque tiene 2 objetos dentro de si Usuario y Profecional creados previamente por fuera de la clase
class DetalleVisita():
    # aca es donde recibe los dos objetos y los alamcena internamente para despues trabajar con ellos
    def __init__(self, usuario: usuario, profesional: profesional, datos_visita: DatosVisita):
        self.user = usuario # aca el atributo user (que esta con el self.user) es = a ususario, lo que significa que user es un objeto Usuario porque al ser = a usuario lo que hago ahi es llamar al parametro del constructor usuario de tipo usuario (usuario:Usuario)
        self.prof = profesional
        self.datos_v = datos_visita
    
    # este metodo simplemente muestra cada uno de los objetos, formateando las cadenas de texto con f
    def mostrar_detalle(self):
        print("\n--- Detalle de la visita ---")
        print(f"Usuario: {self.user.mostrar_nombre()} {self.user.mostrar_apellido()} - DNI: {self.user.mostrar_dni()}")
        print(f"Profesional: {self.prof.mostrar_nombre()} {self.prof.mostrar_apellido()} - DNI: {self.prof.mostrar_dni()} - Especialidad: {self.prof.mostrar_especialidad()}")
        print(f"Motivo de la consulta: {self.user.mostrar_motivo()}")
        print(f"Dia del turno: {self.datos_v.mostrar_dia()}, a la hora: {self.datos_v.mostrar_hora()}, monto a pagar: {self.datos_v.mostrar_monto()}")