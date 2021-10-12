from treelib import Tree, Node
import os, json
from Verification import *

def creaArbol(direccionArchivo):
    arbol = Tree()

    # Nodo raíz con tag e identificador = dirección de la raiz del sistema de archivos
    arbol.create_node(tag = direccionArchivo, identifier=direccionArchivo) 

    #Recorremos el sistema de archivos entero añadiendo al árbol un nodo por cada directorio y carpeta
    for root, dirs, files in os.walk(direccionArchivo, topdown=True):
        for name in files:
            direccion = os.path.join(root, name)
            hashArchivo = hashearArchivo(direccion)
            arbol.create_node(tag = direccion, data=(direccion, hashArchivo), parent = root)
            # para identificar los archivos usaremos una tupla (direccion completa, hash)
            # aunque el show solo muestre el nombre 
        for name in dirs:
            direccion = os.path.join(root, name)
            arbol.create_node(tag = direccion, identifier=direccion, parent = root)
            # para identificar los directorios usaremos la direccion 
    return arbol


