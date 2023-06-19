# 10. **Pesquisa Binária:** A pesquisa binária é uma técnica de pesquisa eficiente que trabalha dividindo repetidamente a lista pela metade. Se a lista está ordenada, a pesquisa binária começa verificando o elemento no meio da lista. Se o elemento do meio é menor do que o item de pesquisa, só a metade superior é necessária e a metade inferior da lista é descartada. Se o elemento do meio é maior, a metade inferior da lista é considerada. Esse processo continua até encontrar o item desejado ou até que não haja mais elementos a serem verificados. A complexidade de tempo da pesquisa binária é O(log n).

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
