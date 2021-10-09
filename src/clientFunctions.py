import socket
from TreeInit import *
HOST = '127.0.0.1'

PORT = 65432

def registroSistema():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"0")

def generarYEnviarArbol(directorio):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"1")
        s.sendall(creaArbol(directorio))

def compruebaArchivos(directorio):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"2")