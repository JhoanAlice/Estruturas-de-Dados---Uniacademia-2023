class Node:
    """
    Esta é a classe de nó que inicializa o valor do nó e define seus filhos como Nenhum.
    """
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    """
    Esta é a função de inserção que adiciona novos nós à árvore binária de busca.
    Se a árvore estiver vazia (root is None), um novo nó será criado.
    Caso contrário, o valor do nó será comparado com a chave e será adicionado ao ramo apropriado.
    """
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def minValueNode(node):
    """
    Esta função retorna o nó com o valor mínimo na árvore ou subárvore dada.
    Ela segue a propriedade da árvore binária de busca onde o valor mais à esquerda é o mínimo.
    """
    current = node

    while(current.left is not None):
        current = current.left

    return current


def deleteNode(root, key):
    """
    Esta é a função que deleta um nó da árvore.
    A função percorre a árvore até encontrar o nó a ser deletado.
    Então, substitui esse nó pelo nó mais à direita de sua subárvore esquerda ou o nó mais à esquerda de sua subárvore direita.
    """
    if root is None:
        return root

    if key < root.val:
        root.left = deleteNode(root.left, key)

    elif(key > root.val):
        root.right = deleteNode(root.right, key)

    else:
        if root.left is None:
            return root.right

        elif root.right is None:
            return root.left

        root.val = minValueNode(root.right).val

        root.right = deleteNode(root.right, root.val)

    return root


def inorder(root):
    """
    Esta é a função de travessia inorder.
    A travessia inorder de uma árvore binária de busca resulta em uma sequência ordenada.
    """
    if root:
        inorder(root.left)
        print(root.val),
        inorder(root.right)


def search(root, key):
    """
    Esta é a função de busca. 
    Ela verifica se o valor do nó é igual à chave. 
    Se não for, verifica se a chave é maior ou menor e decide qual ramo percorrer.
    """
    if root is None or root.val == key:
        return root

    if root.val < key:
        return search(root.right, key)

    return search(root.left, key)


root = None
root = insert(root, 50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)

# Aqui nós imprimimos a árvore usando travessia inorder.
print("Inorder traversal of the given tree")
inorder(root)

# Nós deletamos alguns nós e mostramos a árvore após cada deleção.
print("\nDelete 20")
root = deleteNode(root, 20)
print("Inorder traversal of the modified tree")
inorder(root)

print("\nDelete 30")
root = deleteNode(root, 30)
print("Inorder traversal of the modified tree")
inorder(root)

print("\nDelete 50")
root = deleteNode(root, 50)
print("Inorder traversal of the modified tree")
inorder(root)

# Realizamos uma busca por um valor específico na árvore.
print("\nSearch 40")
node = search(root, 40)
if node:
    print("Found", node.val)
else:
    print("Not found")

# Esse script implementa uma árvore binária de busca completa com as operações de inserção, remoção, busca e travessia inorder. Ele cria uma árvore, insere alguns nós, exibe a árvore usando a travessia inorder, remove alguns nós e exibe a árvore modificada, depois busca um nó específico.

# Lembre-se que as árvores binárias de busca têm a propriedade de que todos os nós à esquerda de um nó têm valores menores que ele, enquanto todos os nós à direita de um nó têm valores maiores que ele. Esta propriedade é mantida após as operações de inserção e remoção.
