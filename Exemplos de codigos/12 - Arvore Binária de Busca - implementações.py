# Arvore Binária de Busca: implementações
# Nó da arvore

class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        # Quando um novo objeto NodoArvore é criado, os valores de chave, esquerda e direita são atribuídos
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        # A função __repr__ define como um objeto NodoArvore será exibido quando impresso
        return '<- %s - %s - %s ->' % (
            self.esquerda and self.esquerda.chave,  # Se existe um nó à esquerda, imprime a chave
            self.chave,
            self.direita and self.direita.chave)  # Se existe um nó à direita, imprime a chave

# Cria um nó raiz com a chave 3
raiz = NodoArvore(3)

# Cria um nó à esquerda da raiz com a chave 5
raiz.esquerda = NodoArvore(5)

# Cria um nó à direita da raiz com a chave 1
raiz.direita = NodoArvore(1)

print("Árvore: ", raiz)  # Imprime a árvore
