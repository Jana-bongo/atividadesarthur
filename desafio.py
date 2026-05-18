def criar_no(valor):
    return {'valor': valor, 'esquerda': None, 'direita': None}

def inserir(no, valor):
    if no is None:
        return criar_no(valor)
    if valor < no['valor']:
        no['esquerda'] = inserir(no['esquerda'], valor)
    elif valor > no['valor']:
        no['direita'] = inserir(no['direita'], valor)
    return no

def altura(no):
    if no is None:
        return 0
    return 1 + max(altura(no['esquerda']), altura(no['direita']))

raiz = None
for v in [50, 30, 70, 20, 40, 60, 80]:
    raiz = inserir(raiz, v)

print("Altura da arvore:", altura(raiz))
print("(esperado: 3 niveis)")