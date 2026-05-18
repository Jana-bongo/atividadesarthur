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
        print("Valor nao encontrado!")
        return False
    print("Comparando com:", no['valor'])
    if valor == no['valor']:
        print("Encontrado!")
        return True
    elif valor < no['valor']:
        return buscar(no['esquerda'], valor)
    else:
        return buscar(no['direita'], valor)

raiz = None
for v in [50, 30, 70, 20, 40, 60, 80]:
    raiz = inserir(raiz, v)

print("Buscando o valor 60...")
print("---")
buscar(raiz, 60)