from Sistema import Usuario, Profesional, datos_visita, detalle_visita

def main():
    # aca inicializo ambos objetos
    usuario = Usuario()
    profesional = Profesional()

    print("--- Ingreso de datos del usuario ---")
    usuario.ingresar_datos() # aca llama mediante el usuario objeto a su metodo para agregar los datos

    print("\n--- Ingreso de datos del profesional ---")
    profesional.ingresar_datos() # lo mismo que en usuario pero con profecional

    print("\n--- Ingreso de datos del turno ---")
    datos = datos_visita() # creo un objeto dia_hora para poder agregar el detetalle del turno
    datos.ingresar_dia()
    datos.ingresar_hora()
    datos.ingresar_monto()

    visita = detalle_visita(usuario, profesional, datos) # y aca lo que hago es crear un objeto vista donde es igual a lo que retorna la clase detalle_vista, con ambos objetos como parametros
    visita.mostrar_detalle() 

if __name__ == "__main__":
    main()
