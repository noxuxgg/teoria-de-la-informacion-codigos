#By Freddy Fernando Huanca Irahola
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

vector_prob.sort(reverse=True)
codigos = shannon_fano_r(vector_prob, alfabeto)

print("\nCódigos Fano-Shanon")
print("X = ",codigos)
