class DatosVisita:
    def __init__(self, dia="", hora="", monto=""):  #constructor para inicializar los atributos
        self._dia = dia
        self._hora = hora
        self._monto = monto

    def ingresar_datos(self):
        self._dia = input("Ingrese el día de la visita: ")
        self._hora = input("Ingrese la hora de la visita: ")
        self._monto = input("Ingrese el monto a pagar: ")

    def mostrar_dia(self):
        return self._dia

    def mostrar_hora(self):
        return self._hora

    def mostrar_monto(self):
        return self._monto
