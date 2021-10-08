import sys, os, json
from TreeInit import *

def creaDirectorio(id):
    try:
        os.mkdir("./Users/" + str(id))
    except OSError:
        print ("No se pudo crear la carpeta")
    else:
        print ("Carpeta creada correctamente")


def inicializaArbolUsuario(id):
    creaDirectorio(id)


creaDirectorio(12)