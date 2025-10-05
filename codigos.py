# By Freddy Fernando Huanca Irahola
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

r = int(input("Ingrese el numero de la fuente: "))
vector_fuente = []
for i in range(1, r + 1):
    m = int(input(f"Ingrese la fuente de r simbolos {i}: "))
    vector_fuente.append(m)
vector_fuente.sort()
s = int(input("Ingrese el numero de simbolos: "))
vector_prob = []
for i in range(1, s + 1):
    p = float(input(f"Ingrese la probabilida de S{i}: "))
    vector_prob.append(p)

for i in range(ficticio(r, vector_prob)):
    vector_prob.append(0)
vector_prob.sort()

nodos = []
for i in range(len(vector_prob)):
    simbolo = f"S{i+1}"
    prob = vector_prob[i]
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

for s in simbolos_finales:
    print(s)
