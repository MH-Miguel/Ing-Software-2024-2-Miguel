#Martínez Herrera Miguel Agustín

def montañasValles(lista):
    contador = 0;
    montañas = 0
    valles = 0
    for i in lista:
        if (i == "U") & (contador == 0):
            montañas+=1
            contador+=1
        elif (i == "U"):
            contador+=1
        elif (i == "D") & (contador == 0):
            valles +=1
            contador-=1
        elif (i == "D"):
            contador-=1
    print(f"contador: {contador}")
    print(f"Montañas: {montañas}")
    print(f"Valles: {valles}")

#Ejemplos:
# list = ["D", "D", "U", "U","U","U", "D", "U","D","U","D","D","D"]
# montañasValles(list);

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.nodo_izquierdo = None
        self.nodo_derecho = None
        self.nodo_padre = None

class ArbolBinarioOrdenado:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self.insertar_aux(valor, self.raiz)

    def insertar_aux(self, valor, nodo_actual):
        if valor <= nodo_actual.valor:
            if nodo_actual.nodo_izquierdo is None:
                nuevo_nodo = Nodo(valor)
                nodo_actual.nodo_izquierdo = nuevo_nodo
                nuevo_nodo.nodo_padre = nodo_actual
            else:
                self.insertar_aux(valor, nodo_actual.nodo_izquierdo)
        elif valor > nodo_actual.valor:
            if nodo_actual.nodo_derecho is None:
                nuevo_nodo = Nodo(valor)
                nodo_actual.nodo_derecho = nuevo_nodo
                nuevo_nodo.nodo_padre = nodo_actual
            else:
                self.insertar_aux(valor, nodo_actual.nodo_derecho)
    

    def preorden(self, nodo):
        if nodo is None:
            return []
        else:
            return [nodo.valor]+self.preorden(nodo.nodo_izquierdo)+self.preorden(nodo.nodo_derecho)

    def inorden(self, nodo):
        if nodo is None:
            return []
        else:
            return self.inorden(nodo.nodo_izquierdo)+[nodo.valor]+self.inorden(nodo.nodo_derecho)

    def postorden(self, nodo):
        if nodo is None:
            return []
        else:
            return self.postorden(nodo.nodo_izquierdo)+self.postorden(nodo.nodo_derecho)+[nodo.valor]

# Ejemplos:
# arbol = ArbolBinarioOrdenado()
# arbol.insertar(5)
# arbol.insertar(3)
# arbol.insertar(3)
# arbol.insertar(2)
# arbol.insertar(4)

# print(f"Los nodos en recorrido preorden son: {arbol.preorden(arbol.raiz)}")
# print(f"Los nodos en recorrido inorden son: {arbol.inorden(arbol.raiz)}")
# print(f"Los nodos en recorrido postorden son: {arbol.postorden(arbol.raiz)}")
