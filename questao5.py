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

def buscar(no, valor):
    if no is None:
        return False
    if valor == no['valor']:
        return True
    elif valor < no['valor']:
        return buscar(no['esquerda'], valor)
    else:
        return buscar(no['direita'], valor)

def em_ordem(no):
    if no is None:
        return
    em_ordem(no['esquerda'])
    print(no['valor'], end=' ')
    em_ordem(no['direita'])

def menor_valor(no):
    while no['esquerda'] is not None:
        no = no['esquerda']
    return no['valor']

def remover(no, valor):
    if no is None:
        return None
    if valor < no['valor']:
        no['esquerda'] = remover(no['esquerda'], valor)
    elif valor > no['valor']:
        no['direita'] = remover(no['direita'], valor)
    else:
        if no['esquerda'] is None and no['direita'] is None:
            return None
        elif no['esquerda'] is None:
            return no['direita']
        elif no['direita'] is None:
            return no['esquerda']
        else:
            sucessor = menor_valor(no['direita'])
            no['valor'] = sucessor
            no['direita'] = remover(no['direita'], sucessor)
    return no

def altura(no):
    if no is None:
        return 0
    return 1 + max(altura(no['esquerda']), altura(no['direita']))

# ── TESTES ──
raiz = None
for v in [50, 30, 70, 20, 40, 60, 80]:
    raiz = inserir(raiz, v)

print("In-Order:", end=' ')
em_ordem(raiz)
print()

print("Busca 60:", buscar(raiz, 60))
print("Busca 99:", buscar(raiz, 99))
print("Altura:", altura(raiz))

raiz = remover(raiz, 20)
raiz = remover(raiz, 30)
raiz = remover(raiz, 70)

print("In-Order apos remocoes:", end=' ')
em_ordem(raiz)
print()