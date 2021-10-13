from treelib import Tree, Node

#DEVOLVER UN TIPO ARBOL A PARTIR DE UN DICCIONARIO
def treeFromDict(dicc):
    raiz = next(iter(dicc))
    res = Tree()
    if dicc[raiz]['data']: #SI EL ELEMENTO QUE TRATAMOS ES UN FICHERO NECESITAMOS INCLUIR EL VALOR QUE TENGA DATA
        res.create_node(tag = raiz, identifier = tuple(dicc[raiz]['data']))  
    else:
        res.create_node(tag = raiz, identifier = raiz)
    if('children' in dicc[raiz]):
        for hijo in dicc[raiz]['children']: 
            subarbol = treeFromDict(hijo)
            res.paste(raiz, subarbol)
    return res
