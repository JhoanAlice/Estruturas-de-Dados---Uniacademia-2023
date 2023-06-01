from typing import List

def quick_sort(arr: List[int], low: int, high: int) -> None:
    """
    Esta função implementa o algoritmo Quick Sort com particionamento e ordenação divididos.
    Ela ordena in-place a sublista de arr delimitada pelos índices low e high.
    """

    if low < high:
        # pi é a posição de pivô após a partição
        pi = partition(arr, low, high)

        # Ordena separadamente os elementos antes e depois da partição
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr: List[int], low: int, high: int) -> int:
    """
    Esta função é uma subfunção do Quick Sort.
    Ela faz a partição dos elementos usando o último elemento como pivô.
    Coloca o elemento pivô em sua posição correta na lista ordenada.
    Coloca todos os elementos menores que o pivô à esquerda do pivô
    e todos os elementos maiores à direita do pivô.
    """

    pivot = arr[high]
    i = low - 1  # Índice do elemento menor

    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Para usar esta versão do Quick Sort, você chamaria quick_sort(arr, 0, len(arr) - 1), onde arr é a lista que você deseja ordenar. Essa implementação do Quick Sort usa a estratégia de escolher o último elemento como pivô e faz a partição in-place (ou seja, sem criar novas listas).