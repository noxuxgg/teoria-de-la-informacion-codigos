#By Freddy Fernando Huanca Irahola
from collections import deque
class Nodo:
    def __init__(self, valor=None, prob=None):
        self.valor = valor
        self.prob = prob
        self.hijos = []
    def __repr__(self):
        return f"{self.valor or 'N'}({self.prob or ''})"

def mostrar_arbol(nodo, nivel=0):
    print("   " * nivel + f"• {nodo.valor}")
    for hijo in nodo.hijos:
        mostrar_arbol(hijo, nivel + 1)

def generar_codigos(alfabeto, N):
    q = deque([""])
    while len(q) < N:
        hoja = q.popleft()
        hijos = [hoja + s for s in alfabeto]
        q.extend(hijos)
    return [q.popleft() for _ in range(N)]

r = int(input("Ingrese el numero de la fuente: "))
vector_fuente = []
for i in range(1, r + 1):
    m = input(f"Ingrese la fuente de r simbolos {i}: ")
    vector_fuente.append(m)
s = int(input("Ingrese el numero de simbolos: "))
codigos = generar_codigos(vector_fuente, s)
print("\nCódigos Fano:")
print("X =", codigos)