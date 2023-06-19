def scan(alist, key):
    N = len(alist)  # Obtém o tamanho da lista alist
    for i in range(0, N):  # Itera sobre todos os elementos da lista
        if alist[i] == key:  # Se o elemento na posição i é igual à chave, retorna o índice
            return i
        elif key < alist[i]:  # Se a chave é menor que o elemento na posição i, a chave não está na lista
            return -1  # Retorna -1 para indicar que a chave não foi encontrada
    return -1  # Retorna -1 se a chave não foi encontrada após percorrer toda a lista
