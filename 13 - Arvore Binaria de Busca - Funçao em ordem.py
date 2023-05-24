# ● Arvore Binária de Busca: implementações
# Função em ordem

class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        # Quando um novo objeto NodoArvore é criado, os valores de chave, esquerda e direita são atribuídos
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        # A função __repr__ define como um objeto NodoArvore será exibido quando impresso
        return '%s' % self.chave

# Cria um nó raiz com a chave 40
raiz = NodoArvore(40)

# Cria nós à esquerda e à direita do nó raiz
raiz.esquerda = NodoArvore(20)
raiz.direita = NodoArvore(60)

# Cria nós à esquerda e à direita do nó à direita do nó raiz
raiz.direita.esquerda = NodoArvore(50)
raiz.direita.direita = NodoArvore(70)

# Cria nós à esquerda e à direita do nó à esquerda do nó raiz
raiz.esquerda.esquerda = NodoArvore(10)
raiz.esquerda.direita = NodoArvore(30)

def em_ordem(raiz):
    """
    Função que imprime os elementos de uma árvore binária de busca em ordem.
    A ordem é definida como: esquerda, raiz, direita.
    """
    # Se a árvore estiver vazia, retorna e não faz nada
    if raiz is None:
        return
    
    # Visita o filho da esquerda
    em_ordem(raiz.esquerda)

    # Visita o nó atual e imprime sua chave
    print(raiz.chave, end=' ')

    # Visita o filho da direita
    em_ordem(raiz.direita)

print("Árvore em ordem: ", end='')
em_ordem(raiz)
