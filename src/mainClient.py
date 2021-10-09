from clientFunctions import *
import sched, time
def __main__():
    print("BIENVENIDO")
    print("opciones:")
    print("1: Registrarse en el sistema")
    print("2: -----------")
    print("3: -----------")
    while True:
        comando = input("Seleccione la opcion deseada\n")
        try:
            comando = int(comando)
        except ValueError:
            print("Introduzca un valor correcto")

        if comando == 1:
            registroSistema()
        elif comando == 2:
            ruta = input("Introduzca la ruta a monitorizar")
            generarYEnviarArbol(ruta)

        elif comando == 3:
            print("Comprobacion de archivos activada cada 24 horas")
            def verificarIntegridad(sc):
                sc.enter(2, 1, verificarIntegridad, (sc,))
                compruebaArchivos()
                

            s = sched.scheduler(time.time, time.sleep)

            s.enter(2, 1, verificarIntegridad, (s,))
            s.run()

        
        else:
            print("Introduzca una opcion correcta")




__main__()