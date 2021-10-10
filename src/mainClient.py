from clientFunctions import *
import sched, time
def __main__():
    ruta = None
    print("BIENVENIDO")
    print("opciones:")
    print("1: Registrarse en el sistema")
    print("2: Seleccionar el directorio a monitorizar")
    print("3: Comenzar la monitorizacion diaria de archivos")
    while True:
        comando = input("Seleccione la opcion deseada\n")
        try:
            comando = int(comando)
        except ValueError:
            print("Introduzca un valor correcto\n")

        if comando == 1:
            registroSistema()
        elif comando == 2:
            ruta = input("Introduzca la ruta a monitorizar\n")
            generarYEnviarArbol(ruta)

        elif comando == 3:
            if ruta == None:
                print("Antes de empezar la monitorizacion, seleccione una ruta")
            else:
                print("Comprobacion de archivos activada cada 24 horas\n")
                def verificarIntegridad(sc, ruta):
                    sc.enter(2, 1, verificarIntegridad, (sc, ruta))
                    compruebaArchivos(ruta)
                
            
            s = sched.scheduler(time.time, time.sleep)

            s.enter(2, 1, verificarIntegridad, (s, ruta ))
            s.run()

        
        else:
            print("Introduzca una opcion correcta")




__main__()