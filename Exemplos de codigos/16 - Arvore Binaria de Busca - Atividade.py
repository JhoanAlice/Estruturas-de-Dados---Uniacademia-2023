# Atividades
# ● Implemente a arvore binária de busca para que ela
# seja capaz de retornar se os elementos abaixo
# estão ou não no vetor arr
# – -50, 54, 71, 19 e 100
# – Vetor arr dado é:
# ● arr = [22, 63, 54, 71, 19, 37];

class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        # Inicializa um novo nodo da árvore com a chave dada e referências vazias para os nodos filhos
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        # Define a representação do nodo quando impresso
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
            raiz.direita = insere(raiz.direita, nodo)
        else:
            raiz.esquerda = insere(raiz.esquerda, nodo)
    
    # Retorna a raiz atualizada
    return raiz

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

arr = [22, 63, 54, 71, 19, 37]
raiz = NodoArvore(40)

# Insere os elementos do vetor arr na árvore binária de busca
for chave in arr:
    nodo = NodoArvore(chave)
    raiz = insere(raiz, nodo)

# Lista de chaves a serem buscadas na árvore
chaves_procuradas = [-50, 54, 71, 19, 100]

# Busca as chaves na árvore e informa se foram encontradas
for chave in chaves_procuradas:
    nodo_encontrado = busca(raiz, chave)
    if nodo_encontrado is None:
        print("Chave {} não encontrada na árvore".format(chave))
    else:
      print("Chave {} encontrada na árvore".format(chave))

