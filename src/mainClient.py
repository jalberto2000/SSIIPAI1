import sched, time, socket, json
from TreeInit import *
from Users import *
from treeFormatter import *

HOST = '127.0.0.1'
FORMATO = "utf-8"
CABECERA = 16
CERRAR_CONEXION = "close_connection"
PORT = 65432
FALLO_VERIFICACION = "123"


def registroSistema():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        enviarMensaje("1", s)
        enviarMensaje(CERRAR_CONEXION, s)
        s.close()

def generarYEnviarArbol(directorio):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        enviarMensaje("2", s)
        enviarMensaje(json.dumps(creaArbol(directorio).to_dict(with_data= True)), s)
        enviarMensaje(CERRAR_CONEXION, s)
        s.close()

#FUNCION QUE IMPLEMENTA EL PROTOCOLO DE PROOF OF POSSESSION
def compruebaArchivos(directorio):
    dicc = {}
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        enviarMensaje("3", s)
        for root, _, files in os.walk(directorio, topdown = True):
            for name in files:
                direccion = os.path.join(root, name)
                hashArchivo = hashearArchivo(direccion)
                token = generadorToken()
                dicc[direccion] = (hashArchivo, token)

        enviarMensaje(json.dumps(dicc), s)
        mensaje_recibido = s.recv(CABECERA)
        datos = s.recv(int(mensaje_recibido.decode(FORMATO))).decode(FORMATO) #RECIBIMOS LOS MACS QUE HA CALCULADO EL SERVIDOR
        diccServidor = json.loads(datos)
        compruebaMACS(diccServidor, dicc)
        enviarMensaje(CERRAR_CONEXION, s)

#VERIFICAMOS LOS MACS QUE ENVIA EL SERVIDOR CON LOS QUE NOSOTROS HEMOS CALCULADO
def compruebaMACS(diccServidor, diccCliente):
    ip = socket.gethostbyname(HOST)
    creaLog(ip)
    for archivo in diccServidor.keys():
        insertaLog(diccServidor[archivo] == calculaMAC(diccCliente[archivo][1], diccCliente[archivo][0]), ip, archivo)

#PROTOCOLO DE ENVIO DE DATOS AL SERVIDOR, PRIMERO SE INDICA EL NUMERO DE BYTES Y LUEGO SE MANDA EL MENSAJE COMO TAL
def enviarMensaje(mensaje, cliente):
    bytesMensaje = mensaje.encode(FORMATO)
    datos_cabecera = str(len(bytesMensaje)).encode(FORMATO)
    datos_cabecera += b' ' * (CABECERA - len(datos_cabecera))
    cliente.send(datos_cabecera)
    cliente.send(bytesMensaje)



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
                    sc.enter(86400, 1, verificarIntegridad, (sc, ruta))
                    compruebaArchivos(ruta)
                    print("Analisis completo")
            s = sched.scheduler(time.time, time.sleep)

            s.enter(2, 1, verificarIntegridad, (s, ruta))
            s.run()

        
        else:
            print("Introduzca una opcion correcta")



            
__main__()