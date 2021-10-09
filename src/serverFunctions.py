import socket

HOST = "127.0.0.1"
PORT = 65432




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