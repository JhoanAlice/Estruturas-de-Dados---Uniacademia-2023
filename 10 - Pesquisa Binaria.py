def iterativeBinarySearch(alist, key):
    N = len(alist)  # Obtém o tamanho da lista alist
    low = 0  # Inicializa a posição de baixo com 0
    high = N - 1  # Inicializa a posição de cima com N - 1

    while low <= high:  # Enquanto a posição de baixo for menor ou igual à posição de cima
        mid = (low + high) // 2  # Calcula a posição do meio
        if alist[mid] == key:  # Se o elemento na posição do meio é igual à chave, retorna o índice
            return mid
        elif key < alist[mid]:  # Se a chave é menor que o elemento na posição do meio, ajusta a posição de cima
            high = mid - 1
        else:  # Se a chave é maior que o elemento na posição do meio, ajusta a posição de baixo
            low = mid + 1
    return -1  # Retorna -1 se a chave não foi encontrada
