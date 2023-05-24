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
    if raiz is None:
        raiz = nodo
    else:
        if raiz.chave < nodo.chave:
            if raiz.direita is None:
                raiz.direita = nodo
            else:
                insere(raiz.direita, nodo)
        else:
            if raiz.esquerda is None:
                raiz.esquerda = nodo
            else:
                insere(raiz.esquerda, nodo)

def busca(raiz, chave):
    """
    Função para procurar uma chave em uma árvore binária de busca.
    Se a chave for encontrada, retorna o nodo correspondente. Caso contrário, retorna None.
    """
    if raiz is None:
        # A chave não foi encontrada na árvore
        return None
    if raiz.chave == chave:
        # A chave foi encontrada na raiz da árvore
        return raiz
    if raiz.chave < chave:
        # A chave é maior que a da raiz, então a busca continua na subárvore direita
        return busca(raiz.direita, chave)
    else:
        # A chave é menor que a da raiz, então a busca continua na subárvore esquerda
        return busca(raiz.esquerda, chave)

def em_ordem(raiz):
    if raiz is None:
        return
    em_ordem(raiz.esquerda)
    print(raiz.chave, end=' ')
    em_ordem(raiz.direita)

arr = [22, 63, 54, 71, 19, 37]
raiz = NodoArvore(40)

for chave in arr:
    nodo = NodoArvore(chave)
    insere(raiz, nodo)

print("Árvore em ordem: ", end='')
em_ordem(raiz)

# Realiza uma busca na árvore
chave_procurada = 19
nodo_encontrado = busca(raiz, chave_procurada)
if nodo_encontrado is None:
    print("\nChave {} não encontrada na árvore".format(chave_procurada))
else:
    print("\nChave {} encontrada na árvore".format(chave_procurada))
