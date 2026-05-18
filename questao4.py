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
            print(f"Removendo {valor} - Caso 1: no sem filhos")
            return None
        elif no['esquerda'] is None:
            print(f"Removendo {valor} - Caso 2: no com 1 filho")
            return no['direita']
        elif no['direita'] is None:
            print(f"Removendo {valor} - Caso 2: no com 1 filho")
            return no['esquerda']
        else:
            print(f"Removendo {valor} - Caso 3: no com 2 filhos")
            sucessor = menor_valor(no['direita'])
            no['valor'] = sucessor
            no['direita'] = remover(no['direita'], sucessor)
    return no

raiz = None
for v in [50, 30, 70, 20, 40, 60, 80]:
    raiz = inserir(raiz, v)

print("Antes de qualquer remocao:")
em_ordem(raiz)
print()

raiz = remover(raiz, 20)
print("Depois de remover 20:")
em_ordem(raiz)
print()

raiz = remover(raiz, 30)
print("Depois de remover 30:")
em_ordem(raiz)
print()

raiz = remover(raiz, 70)
print("Depois de remover 70:")
em_ordem(raiz)
print()
#kk quebrei um pouco minha cabeça nessa