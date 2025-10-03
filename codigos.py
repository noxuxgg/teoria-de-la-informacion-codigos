def ficticio(r, vector):
    q = len(vector)
    izq = 0
    alfa = 0
    while izq < q:
        izq = r + alfa* (r-1)    
        alfa = alfa+1
    res = izq - q
    return res

def sumar_r(r, vector):
    print(vector)
    while r != len(vector):
        suma = 0
        cont = 0
        while cont != r:
            suma = suma + vector[0]
            vector.pop(0)    
            cont = cont + 1
        vector.append(round(suma,5))
        vector.sort()
        print(vector)

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
print("Fuente: ",vector_fuente)
for i in range(0,ficticio(r,vector_prob)):
    vector_prob.append(0)
vector_prob.sort()
print("Suma r: ")
sumar_r(r, vector_prob)