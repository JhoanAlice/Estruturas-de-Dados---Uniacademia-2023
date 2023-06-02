class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


def search(root, key):
    if root is None or root.val == key:
        return root

    if root.val < key:
        return search(root.right, key)

    return search(root.left, key)


def minValueNode(root):
    current = root
    while (current.left is not None):
        current = current.left

    return current


def deleteNode(root, key):
    if root is None:
        return root

    if key < root.val:
        root.left = deleteNode(root.left, key)

    elif (key > root.val):
        root.right = deleteNode(root.right, key)

    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minValueNode(root.right)

        root.val = temp.val

        root.right = deleteNode(root.right, temp.val)

    return root


def binary_search_tree(arr: list) -> None:
    r = Node(arr[0])
    for i in range(1, len(arr)):
        r = insert(r, arr[i])

    print("Inorder traversal of the given tree")
    inorder(r)

    print("\nDelete 20")
    r = deleteNode(r, 20)
    print("Inorder traversal of the modified tree")
    inorder(r)

    print("\nDelete 30")
    r = deleteNode(r, 30)
    print("Inorder traversal of the modified tree")
    inorder(r)

    print("\nDelete 50")
    r = deleteNode(r, 50)
    print("Inorder traversal of the modified tree")
    inorder(r)

    print("\nSearch 40")
    res = search(r, 40)
    if res:
        print("Found 40")
    else:
        print("40 Not found")

# Esse script implementa uma árvore binária de busca completa com as operações de inserção, remoção, busca e travessia inorder. Ele cria uma árvore, insere alguns nós, exibe a árvore usando a travessia inorder, remove alguns nós e exibe a árvore modificada, depois busca um nó específico.

# Lembre-se que as árvores binárias de busca têm a propriedade de que todos os nós à esquerda de um nó têm valores menores que ele, enquanto todos os nós à direita de um nó têm valores maiores que ele. Esta propriedade é mantida após as operações de inserção e remoção.
