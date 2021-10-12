from treelib import Tree, Node
def treeFromDict(dicc):
    raiz = next(iter(dicc))
    res = Tree()
    print(dicc[raiz]['data'])
    if dicc[raiz]['data']:
        res.create_node(tag = raiz, identifier = tuple(dicc[raiz]['data']))
    else:
        res.create_node(tag = raiz, identifier = raiz)
    if('children' in dicc[raiz]):
        for hijo in dicc[raiz]['children']: 
            subarbol = treeFromDict(hijo)
            res.paste(raiz, subarbol)
    return res

def tupleFromStr(st):
    return tuple(st[1 : len(st) -1].split(', '))