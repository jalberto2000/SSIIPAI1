import socket

HOST = "127.0.0.1"
PORT = 65432
CABECERA = 16
FORMATO = "utf-8"
CERRAR_CONEXION = "close_connection"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

def arrancar_servidor():
    server.listen()
    while True:
        conn, direccion = server.accept()
        manejar_cliente(conn, direccion)

def manejar_cliente(conn, direccion):
    print("Nueva conexion con: " + str(direccion))
    while True:
        mensaje_recibido = conn.recv(CABECERA) 
        if mensaje_recibido:
            datos = conn.recv(int(mensaje_recibido.decode(FORMATO))).decode(FORMATO)
            print(datos)
            if datos == CERRAR_CONEXION:
                break
    
    conn.close()

    pass


arrancar_servidor()
"""
def __main__():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()

            with conn:
                print('Conectado con: ', addr)
                
                datos = conn.recv(4096)
                if not datos:
                    break
                if datos == 0:
                    #TODO FUNCION QUE REGISTRA AL USUARIO
                    conn.sendall(b'El registro se ha realizado correctamente\n')
                    
                if datos == 1:
                    #TODO FUNCION QUE GUARDA EL ARBOL DEL USUARIO EN SU CARPETA
                    conn.sendall(b'El sistema esta listo para guardar los archivos\n')

                if datos == 2:
                    '''
                    TODO FUNCION QUE RECIBE EL HASH, EL ARCHIVO Y EL TOKEN, CALCULA EL MAC
                    Y DEVUELVE SI EL HASH COINCIDE
                    '''
                    conn.sendall(b'Iniciando comprobacion de archivos')

    

__main__()


"""