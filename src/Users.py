import sys, os, json
from TreeInit import *
from datetime import datetime


def creaUsuario(id):
    try:
        os.mkdir("./Users/" + str(id))
    except OSError:
        print ("No se pudo crear el usuario")
    else:
        print ("Usuario creado")



def creaLog(id):
    fecha = datetime.now().strftime("%d/%m/%Y")
    mes = datetime.now().strftime("%m %Y")
    hora = datetime.now().strftime("%H:%M:%S")
    direccionUsuario = "./Users/" + str(id)
    f = open(direccionUsuario + "/" + mes +".txt","a+")
    f.write("Analisis realizado el dia " + fecha + " a las " + hora + "\n")
    f.close()


def insertaLog(status, id, direccion):
    fecha = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    mes = datetime.now().strftime("%m %Y")
    direccionUsuario = "./Users/" + str(id) 
    if status:
        f = open(direccionUsuario + "/" + mes +".txt","a+")
        f.write("El archivo: " + direccion + " esta integro \n")
        f.close()
    else:
        f = open(direccionUsuario + "/" + mes +".txt","a+")
        f.write("El archivo: " + direccion + " ha sido modificado \n")
        f.close()







