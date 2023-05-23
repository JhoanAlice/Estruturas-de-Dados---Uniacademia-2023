# 9. **Pesquisa Sequencial:** Esta é a técnica de pesquisa mais simples. Ele começa do primeiro item de uma lista e continua a percorrer cada elemento sequencialmente até encontrar um correspondente ou até ter verificado todos os itens. É fácil de entender e implementar. No entanto, para listas grandes, a pesquisa sequencial pode ser ineficiente, pois, na pior das hipóteses, cada elemento da lista precisa ser verificado. A complexidade de tempo da pesquisa sequencial é O(n)

def scan(alist, key):
    N = len(alist)  # Obtém o tamanho da lista alist
    for i in range(0, N):  # Itera sobre todos os elementos da lista
        if alist[i] == key:  # Se o elemento na posição i é igual à chave, retorna o índice
            return i
        elif key < alist[i]:  # Se a chave é menor que o elemento na posição i, a chave não está na lista
            return -1  # Retorna -1 para indicar que a chave não foi encontrada
    return -1  # Retorna -1 se a chave não foi encontrada após percorrer toda a lista
