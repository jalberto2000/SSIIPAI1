import socket
from TreeInit import *  
HOST = '127.0.0.1'
FORMATO = "utf-8"
CERRAR_CONEXION = "close_connection"
CABECERA = 16
PORT = 65432

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

def enviarMensaje(mensaje):
    bytesMensaje = mensaje.encode(FORMATO)
    datos_cabecera = str(len(bytesMensaje)).encode(FORMATO)
    datos_cabecera += b' ' * (CABECERA - len(datos_cabecera))
    cliente.send(datos_cabecera)
    cliente.send(bytesMensaje)

enviarMensaje("Hola")
enviarMensaje("probando servidor cliente")
enviarMensaje(CERRAR_CONEXION)



def registroSistema():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"0")
        s.close()

def generarYEnviarArbol(directorio):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"1")
        respuesta = s.recv(1024)
        s.sendall(str(creaArbol(directorio).to_dict()).encode("utf8"))
        s.close()

#TODO TERMINAR EL PROTOCOLO A LA HORA DE VERIFICAR LA INTEGRIDAD DEL ARCHIVO
def compruebaArchivos(directorio):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"2")
        respuesta = s.recv(1024)
        for root, _, files in os.walk(directorio, topdown = True):
            for name in files:
                direccion = os.path.join(root, name)
                hashArchivo = hashearArchivo(direccion)
                token = generadorToken()
                s.sendall(str(direccion), str(hashArchivo), str(token)).encode("utf8")
                verificacionHash = int(s.recv(4096))
                if not verificacionHash:
                    print("Fallo en el archivo")
                else:
                    print("Comprobar MAC del archivo")

        s.close()
