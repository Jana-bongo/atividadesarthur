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

def em_ordem(no):
    if no is None:
        return
    em_ordem(no['esquerda'])
    print(no['valor'], end=' ')
    em_ordem(no['direita'])

raiz = None
for v in [50, 30, 70, 20, 40, 60, 80]:
    raiz = inserir(raiz, v)

print("Percurso In-Order:")
em_ordem(raiz)
print()