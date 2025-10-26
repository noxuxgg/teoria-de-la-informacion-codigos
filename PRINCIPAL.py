# By Freddy Fernando Huanca Irahola
from collections import deque

# FANO
def generar_codigos(alfabeto, N):
    q = deque([""])
    while len(q) < N:
        hoja = q.popleft()
        hijos = [hoja + s for s in alfabeto]
        q.extend(hijos)
    return [q.popleft() for _ in range(N)]

# FANO SHANNON
def shannon_fano_r(probabilidades, alfabeto):
    n = len(probabilidades)
    r = len(alfabeto)
    if n == 1:
        return [""]

    total = sum(probabilidades)
    grupos = []
    inicio = 0

    while inicio < n:
        acc = 0
        fin = inicio
        while fin < n and acc + probabilidades[fin] <= total / r:
            acc += probabilidades[fin]
            fin += 1
        if fin == inicio:
            fin += 1
        grupos.append((inicio, fin))
        inicio = fin

    if len(grupos) > r:
        extra = len(grupos) - r
        for _ in range(extra):
            i1, f1 = grupos.pop(-2)
            i2, f2 = grupos.pop(-1)
            grupos.append((i1, f2))

    codigos = [""] * n
    for idx, (inicio, fin) in enumerate(grupos):
        subcodigos = shannon_fano_r(probabilidades[inicio:fin], alfabeto)
        for j, sub in enumerate(subcodigos):
            codigos[inicio + j] = alfabeto[idx] + sub
    return codigos

# HUFFMAN 
def ficticio(r, vector):
    q = len(vector)
    izq = 0
    alfa = 0
    while izq < q:
        izq = r + alfa * (r - 1)
        alfa += 1
    return izq - q

def sumar_r(r, nodos):
    while len(nodos) > r:
        grupo = nodos[:r]
        suma_prob = sum([n[0] for n in grupo])
        nuevo_nodo = [round(suma_prob, 5), grupo, '']
        nodos = nodos[r:]
        nodos.append(nuevo_nodo)
        nodos.sort(key=lambda x: x[0])
    return nodos

def propagar_codigos(nodo, prefijo=''):
    if isinstance(nodo[1], list):
        for i, hijo in enumerate(nodo[1]):
            propagar_codigos(hijo, prefijo + str(i))
    else:
        nodo[2] = prefijo

def extraer_simbolos(nodo, lista):
    if isinstance(nodo[1], list):
        for hijo in nodo[1]:
            extraer_simbolos(hijo, lista)
    else:
        lista.append(nodo)

# ENTRADA
r = int(input("Ingrese el numero de la fuente: "))
alfabeto = []
for i in range(r):
    s = input(f"Ingrese el símbolo {i+1} de la fuente: ")
    alfabeto.append(s)

s = int(input("Ingrese el numero de simbolos a codificar: "))
vector_prob = []
for i in range(s):
    p = float(input(f"Ingrese la probabilidad de S{i+1}: "))
    vector_prob.append(p)

# FANO
codigos_fano = generar_codigos(alfabeto, s)
print("\nFANO \nX =", codigos_fano)

# FANO SHANNON
vector_prob_sorted = sorted(vector_prob, reverse=True)
codigos_fano_shanon = shannon_fano_r(vector_prob_sorted, alfabeto)
print("FANOSHANON \nX =", codigos_fano_shanon)

# HUFFMAN
vector_prob_huffman = sorted(vector_prob, reverse=True)
for i in range(ficticio(r, vector_prob_huffman)):
    vector_prob_huffman.append(0)
vector_prob_huffman.sort()

nodos = []
for i in range(len(vector_prob_huffman)):
    simbolo = f"S{i+1}"
    prob = vector_prob_huffman[i]
    nodos.append([prob, simbolo, ''])

nodos_finales = sumar_r(r, nodos)

ultimos = nodos_finales[-r:]
ultimos.sort(key=lambda x: x[0], reverse=True)
for i, nodo in enumerate(ultimos):
    propagar_codigos(nodo, str(i))

simbolos_finales = []
for nodo in nodos_finales:
    extraer_simbolos(nodo, simbolos_finales)

simbolos_finales.sort(key=lambda x: x[0], reverse=True)
codigos_huffman = [n[2] for n in simbolos_finales]

print("HUFFMAN \nX =", codigos_huffman)
