import hashlib
import secrets

TAMAÑO_BUFFER = 65536
def hashearArchivo(archivo):

    #UTILIZAMOS UN TAMAÑO DE BUFFER DE 64 KB PARA QUE ARCHIVOS MUY GRANDES NO SATUREN LA MEMORIA
    sha256 = hashlib.sha256()

    with open(archivo, 'rb') as f: #ABRIMOS LOS ARCHIVOS EN MODO BINARIO PARA NO TENER PROBLEMAS CON CARACTERES ESPECIALES
        while True:
            datos = f.read(TAMAÑO_BUFFER)
            if not datos:
                break
            sha256.update(datos)
    return int(sha256.hexdigest(), 16) #DEVOLVEMOS EL HASH DEL ARCHIVO EN HEXADECIMAL

#LA FUNCION GENERADORTOKEN ES UN WRAPPER DE LA FUNCION IMPLEMENTADA EN EL MODULE SECRETS
def generadorToken(n_bits = None):
    return int(secrets.token_hex(n_bits), 16)


def calculaMAC(token, hash):

    llave = str(hash % token) #CALCULAMOS LA LLAVE PARA EL HMAC QUE SERA EN ESTE CASO UN MODULO ENTRE EL HASH Y EL TOKEN


    return llave


