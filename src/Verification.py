import hashlib
import secrets
def hashearArchivo(archivo, TAMAÑO_BUFFER = 65536):

    #UTILIZAMOS UN TAMAÑO DE BUFFER DE 64 KB PARA QUE ARCHIVOS MUY GRANDES NO SATUREN LA MEMORIA
    sha256 = hashlib.sha256()

    with open(archivo, 'rb') as f: #ABRIMOS LOS ARCHIVOS EN MODO BINARIO PARA NO TENER PROBLEMAS CON CARACTERES ESPECIALES
        while True:
            datos = f.read(TAMAÑO_BUFFER)
            if not datos:
                break
            sha256.update(datos)
    return sha256.hexdigest() #DEVOLVEMOS EL HASH DEL ARCHIVO EN HEXADECIMAL

#LA FUNCION GENERADORTOKEN ES UN WRAPPER DE LA FUNCION IMPLEMENTADA EN EL MODULE SECRETS
def generadorToken(n_bits = None):
    return secrets.token_hex(n_bits)


def calculaMAC(token, hash):
    #SUPONGO QUE EL CHALLENGE ES UNA SUMA HASTA QUE CONTESTE EL PROFESOR 
    return (token + hash)
