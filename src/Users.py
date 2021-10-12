import os
from TreeInit import *
from datetime import datetime

#CREA UNA CARPETA EN /USERS CON EL ID APORTADO
def creaUsuario(id):
    try:
        os.mkdir("./Users/" + str(id))
    except OSError:
        print ("No se pudo crear el usuario")
    else:
        print ("Usuario creado")


#AÑADIMOS UNA ENTRADA EN EL LOG DEL USUARIO INDICADO CON FECHA Y HORA
def creaLog(id):
    fecha = datetime.now().strftime("%d/%m/%Y")
    mes = datetime.now().strftime("%m %Y")
    hora = datetime.now().strftime("%H:%M:%S")
    direccionUsuario = "./Users/" + str(id)
    f = open(direccionUsuario + "/" + mes +".txt","a+")
    f.write("Analisis realizado el dia " + fecha + " a las " + hora + "\n")
    f.close()

#POR CADA FICHERO AÑADIMOS UNA LINEA EN EL LOG INDICANDO SI HA SIDO MODIFICADO O NO
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







