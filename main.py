from usuario import Usuario
from profesional import Profesional
from DatosVisita import DatosVisita
from DetalleVisita import DetalleVisita
from personaFabrica import PersonaFabrica

def main():
    # inicializacion
    personas_creadas = [] # Lista para almacenar los objetos creados
    fabrica = PersonaFabrica() # creo objeto de tipo fabrica para despues poder crear personas

    while True:  # ciclo para quev el cliente pueda agregar la cantidad de parsonas que quiera
        tipo = input("Ingrese el tipo de persona que quiere crear (usuario/profesional): ").lower()
        persona = fabrica.crear_persona(tipo)
        persona.ingresar_datos()
        personas_creadas.append(persona)

        continuar = input("¿Desea crear otra persona? (sí/no): ").lower()
        if continuar == "no":
            break

    # esto lo que hace es basicamente separar la lista personas_creadas en dos listas Usuario y Profecional
    usuarios = [p for p in personas_creadas if isinstance(p, Usuario)] # Recorré todos los elementos p en la lista personas_creadas, y se queda solo con aquellos que sean una instancia de la clase Usuario. Guardá ese nuevo conjunto filtrado en la lista usuario, con isinstance puedo verificar que sea usuario y que me cree un usuario
    profesionales = [p for p in personas_creadas if isinstance(p, Profesional)] # lo mismo que arriba

    cant_turnos = min(len(usuarios), len(profesionales)) # esto lo que hace es: 1 len(devuelve la cantidad de objetos que hay); 2 min(devulve la cantidad minima entre ambas listas), lo que permite es ver cuantos usuarios y profecionales hay y crear turnos de acuerdo a esas cantidades

    for i in range(cant_turnos):
        print(f"\n--- Ingreso de datos del turno {i + 1} ---")
        datos = DatosVisita()
        datos.ingresar_datos()

        visita = DetalleVisita(usuarios[i], profesionales[i], datos)
        print(f"\n--- Detalle del turno {i + 1} ---")
        visita.mostrar_detalle()

if __name__ == "__main__":
    main()
