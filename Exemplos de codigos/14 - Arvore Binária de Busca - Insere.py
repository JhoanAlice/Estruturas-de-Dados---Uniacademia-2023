class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s' % self.chave

def insere(raiz, nodo):
    """
    Função para inserir um nodo em uma árvore binária de busca.
    A chave do novo nodo determina onde o nodo será inserido.
    """
    # Se a árvore está vazia, o nodo se torna a raiz
    if raiz is None:
        raiz = nodo
    else:
        # Se a chave do nodo é maior que a chave da raiz, o nodo é inserido na subárvore direita
        if raiz.chave < nodo.chave:
            if raiz.direita is None:
                raiz.direita = nodo
            else:
                insere(raiz.direita, nodo)
        # Se a chave do nodo é menor que a chave da raiz, o nodo é inserido na subárvore esquerda
        else:
            if raiz.esquerda is None:
                raiz.esquerda = nodo
            else:
                insere(raiz.esquerda, nodo)

def em_ordem(raiz):
    if raiz is None:
        return
    em_ordem(raiz.esquerda)
    print(raiz.chave, end=' ')
    em_ordem(raiz.direita)

# Lista de chaves que serão inseridas na árvore
arr = [22, 63, 54, 71, 19, 37]

# Cria a raiz da árvore
raiz = NodoArvore(40)

# Insere cada chave da lista na árvore
for chave in arr:
    nodo = NodoArvore(chave)
    insere(raiz, nodo)

# Imprime o percurso em ordem da árvore
print("Árvore em ordem: ", end='')
em_ordem(raiz)
