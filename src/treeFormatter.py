from treelib import Tree, Node
s = {"Harry": {"data": 1, "children": [{"Bill": {"data": 2}}, {"Jane": {"data": 3, "children": [{"Diane": {"data": 4}}, {"Mark": {"data": 5}}]}}, {"Mary": {"data": 6}}]}}

st = "(hola, adios)"
t = tuple((st[1: len(st)-1].split(', ')))
def treeFromDict(dicc):
    raiz = next(iter(dicc))
    res = Tree()
    res.create_node(tag = raiz, identifier = tupleFromStr(dicc[raiz]['data']))
    if('children' in dicc[raiz]):
        for hijo in dicc[raiz]['children']: 
            subarbol = treeFromDict(hijo)
            res.paste(raiz, subarbol)
    return res

def tupleFromStr(st):
    return tuple(st[1 : len(st) -1].split(', '))