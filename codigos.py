def ficticio(r, vector):
    q = len(vector)
    izq = 0
    alfa = 0
    while izq < q:
        izq = r + alfa* (r-1)    
        alfa = alfa+1
    res = izq - q
    return res








r = int(input("Ingrese el numero de la fuente: "))
vector_fuente = []
for i in range(1, r+1):
    m = int(input("Ingrese la fuente de r simbolos "+str(i)+': '))
    vector_fuente.append(m)
vector_fuente.sort()
s = int(input("Ingrese el numero de simbolos: "))
vector_prob = []
for i in range(1, s+1):
    p = float(input("Ingrese la probabilida de S"+str(i)+': '))
    vector_prob.append(p)
vector_prob.sort()
print(vector_fuente)
print(vector_prob)
print(ficticio(r,vector_prob))