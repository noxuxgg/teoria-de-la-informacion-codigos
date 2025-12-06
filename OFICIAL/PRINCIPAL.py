# By Freddy Fernando Huanca Irahola
from collections import deque
import math

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

entropia = -sum(p * math.log2(p) for p in vector_prob if p > 0)
L_fano = sum(vector_prob[i] * len(codigos_fano[i]) for i in range(len(vector_prob)))
L_fano_shannon = sum(vector_prob_sorted[i] * len(codigos_fano_shanon[i]) for i in range(len(vector_prob_sorted)))
L_huffman = sum(vector_prob[i] * len(codigos_huffman[i]) for i in range(len(vector_prob)))

E_fano = (entropia / L_fano) * 100
E_fano_shannon = (entropia / L_fano_shannon) * 100
E_huffman = (entropia / L_huffman) * 100

print("\n--- RESULTADOS DE EFICIENCIA ---")
print(f"Entropía del conjunto: {entropia:.4f} bits/símbolo")
print(f"Longitud promedio Fano: {L_fano:.4f} -> Eficiencia: {E_fano:.2f}%")
print(f"Longitud promedio Fano-Shannon: {L_fano_shannon:.4f} -> Eficiencia: {E_fano_shannon:.2f}%")
print(f"Longitud promedio Huffman: {L_huffman:.4f} -> Eficiencia: {E_huffman:.2f}%")

eficiencias = {
    "Fano": E_fano,
    "Fano-Shannon": E_fano_shannon,
    "Huffman": E_huffman
}

max_ef = max(eficiencias.values())
mejores = [alg for alg, ef in eficiencias.items() if abs(ef - max_ef) < 1e-9]

print("\nAlgoritmo(s) más eficiente(s):", ", ".join(mejores))
for alg in mejores:
    if alg == "Fano":
        print("Códigos Fano:", codigos_fano)
    elif alg == "Fano-Shannon":
        print("Códigos Fano-Shannon:", codigos_fano_shanon)
    else:
        print("Códigos Huffman:", codigos_huffman)