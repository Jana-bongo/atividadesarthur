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

raiz = None
for v in [50, 30, 70, 20, 40, 60, 80]:
    raiz = inserir(raiz, v)

print("Arvore inserida com sucesso!")
print("Raiz:", raiz['valor'])
print("Filho esquerdo da raiz:", raiz['esquerda']['valor'])
print("Filho direito da raiz:", raiz['direita']['valor'])
print("Filho esquerdo do 30:", raiz['esquerda']['esquerda']['valor'])
print("Filho direito do 30:", raiz['esquerda']['direita']['valor'])
print("Filho esquerdo do 70:", raiz['direita']['esquerda']['valor'])
print("Filho direito do 70:", raiz['direita']['direita']['valor'])