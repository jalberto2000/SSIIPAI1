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
            arbol.create_node(tag = name, identifier=(direccion, hashArchivo), parent = root)
            # para identificar los archivos usaremos una tupla (direccion completa, hash)
            # aunque el show solo muestre el nombre 
        for name in dirs:
            direccion = os.path.join(root, name)
            arbol.create_node(tag = name, identifier=direccion, parent = root)
            # para identificar los directorios usaremos la direccion 
    return arbol


s = '{"Harry": {"data": null, "children": [{"Bill": {"data": null}}, {"Jane": {"data": null, "children": [{"Diane": {"data": null}}, {"Mark": {"data": null}}]}}, {"Mary": {"data": null}}]}}'

def treeFromJson(a):
    res = Tree()
    arbol = json.dumps(a)
    return arbol

arbol = creaArbol(r"C:\Users\a-l-f\Desktop\carpeta1")

print(creaArbol(r"C:\Users\a-l-f\Desktop\carpeta1"))

print(arbol.contains(r'C:\Users\a-l-f\Desktop\carpeta1'))

print(type(s))

print(type(treeFromJson(s)))



creaarbol(diccionario, padre):
    arbol = diccionario.llave
    for hijo en hijos]:
        arbol = añadir creaarbol a arbol
