from typing import List

def bubble_sort(arr: List[int]) -> List[int]:
    """
    Esta função implementa o algoritmo Bubble Sort.
    Recebe uma lista de inteiros e retorna a lista ordenada.
    """

    # Obtenha o número de elementos na lista
    n = len(arr)

    # Percorra todos os elementos da lista
    for i in range(n):

        # Os últimos 'i' elementos já estão no lugar, então percorra de 0 a 'n-i-1'
        for j in range(0, n - i - 1):

            # Troque se o elemento encontrado é maior que o próximo elemento
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# Este código implementa a versão básica do Bubble Sort. Ele percorre a lista várias vezes e a cada passagem, "flutua" o maior elemento não classificado até o topo, colocando-o em sua posição correta. Ele continua fazendo isso até que todos os elementos estejam em suas posições corretas.