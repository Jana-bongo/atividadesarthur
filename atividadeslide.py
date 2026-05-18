def criar_no(valor):
    return {"valor": valor, "esquerda": None, "direita": None}


def inserir(no, valor):
    if no is None:
        return criar_no(valor)
    if valor < no["valor"]:
        no["esquerda"] = inserir(no["esquerda"], valor)
    elif valor > no["valor"]:
        no["direita"] = inserir(no["direita"], valor)
    return no


def buscar(no, valor):
    if no is None:
        return False
    if valor == no["valor"]:
        return True
    elif valor < no["valor"]:
        return buscar(no["esquerda"], valor)
    else:
        return buscar(no["direita"], valor)


def menor_valor(no):
    atual = no
    while atual["esquerda"] is not None:
        atual = atual["esquerda"]
    return atual


def remover(no, valor):
    if no is None:
        return None
    if valor < no["valor"]:
        no["esquerda"] = remover(no["esquerda"], valor)
    elif valor > no["valor"]:
        no["direita"] = remover(no["direita"], valor)
    else:
        if no["esquerda"] is None:
            return no["direita"]
        if no["direita"] is None:
            return no["esquerda"]
        menor = menor_valor(no["direita"])
        no["valor"] = menor["valor"]
        no["direita"] = remover(no["direita"], menor["valor"])
    return no


def em_ordem(no):
    if no is None:
        return
    em_ordem(no["esquerda"])
    print(no["valor"], end=" ")
    em_ordem(no["direita"])

raiz = None

valores = [50, 30, 70, 20, 40, 60, 80]
for valor in valores:
    raiz = inserir(raiz, valor)

print(buscar(raiz, 60))

raiz = remover(raiz, 30)

em_ordem(raiz)