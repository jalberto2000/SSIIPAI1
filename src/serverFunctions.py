import socket, json, treelib
from Users import *
from treeFormatter import *
HOST = "127.0.0.1"
PORT = 65432
CABECERA = 16
FORMATO = "utf-8"
CERRAR_CONEXION = "close_connection"
FALLO_VERIFICACION = "123"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

def enviarMensaje(mensaje, cliente):
    bytesMensaje = mensaje.encode(FORMATO)
    datos_cabecera = str(len(bytesMensaje)).encode(FORMATO)
    datos_cabecera += b' ' * (CABECERA - len(datos_cabecera))
    cliente.send(datos_cabecera)
    cliente.send(bytesMensaje)


def arrancar_servidor():
    server.listen()
    while True:
        conn, direccion = server.accept()
        manejar_cliente(conn, direccion)

def maneja_crea_arbol(conn, direccion):
    mensaje_recibido = conn.recv(CABECERA) 
    ruta_archivo = "./Users/"+ str(direccion[0]+"/arbol")
    if mensaje_recibido:
        datos = conn.recv(int(mensaje_recibido.decode(FORMATO))).decode(FORMATO)
        
        with open(file = ruta_archivo, mode = 'w') as f:
            f.write(datos)

def integridadFicheros(dicc, arbol):
    res = {}
    for direccion in dicc.keys():
        if (arbol.contains((direccion, dicc[direccion][0]))):
            res[direccion] = calculaMAC(dicc[direccion][1], dicc[direccion][0])
        else:
            res[direccion] = FALLO_VERIFICACION
    return res

def manejar_cliente(conn, direccion):
    print("Nueva conexion con: " + str(direccion))
    while True:
        mensaje_recibido = conn.recv(CABECERA) 
        if mensaje_recibido:
            datos = conn.recv(int(mensaje_recibido.decode(FORMATO))).decode(FORMATO)
            if datos == "1":
                creaUsuario(direccion[0])
            elif datos == "2":
                maneja_crea_arbol(conn, direccion)
            elif datos == "3":
                arbol = None
                msj = conn.recv(CABECERA)
                datos_arbol = conn.recv(int(msj.decode(FORMATO))).decode(FORMATO)
                dicc = json.loads(datos_arbol)
                with open("./Users/"+str(direccion[0]) + "/arbol", 'r') as f:
                    arbol = treeFromDict(json.loads(f.read()))
                res = integridadFicheros(dicc, arbol)
                enviarMensaje(json.dumps(res), conn)
                
            if datos == CERRAR_CONEXION:
                break
    
    conn.close()

    pass


arrancar_servidor()