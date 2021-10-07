'''Este codigo sirve para conectar 2 clientes y que se comuniquen entre ellos'''
'''El siguiente paso es conectar mediante una serie de comandos con el servidor (host)'''
import socket
import select
import errno
import sys

header = 10
ip = "127.0.0.1"
port = 1234

identify = input("Introduzca su usuario: ")
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((ip,port))
client_socket.setblocking(False)

username = identify.encode('utf-8')
username_header = f"{len(username):<{header}}".encode('utf-8')
client_socket.send(username_header + username)

while True:
    message = input(f"{identify} > ")
    if message:
        message = message.encode('utf-8')
        message_header = f"{len(message):<{header}}".encode("utf-8")
        client_socket.send(message_header + message)
    try:
        while True:
            username_header=client_socket.recv(header)
            if not len(username_header):
                print("Connection closed by the server")
                sys.exit()

            username_length = int(username_header.decode("utf-8").strip())
            username = client_socket.recv(username_length).decode("utf-8")
            message_header = client_socket.recv(header)
            message_length = int(message_header.decode("utf-8").strip())
            message = client_socket.recv(message_length).decode("utf-8")

            print(f"{username} > {message}")
    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error',str(e))
            sys.exit()
        continue

    except Exception as e:
        print('General error', str(e))
        sys.exit()
