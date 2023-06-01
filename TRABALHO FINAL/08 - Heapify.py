from typing import List

def heapify(arr: List[int], n: int, i: int) -> None:
    """
    Esta função implementa o algoritmo Heapify.
    Ela transforma um array em uma árvore binária completa.

    Args:
        arr: A lista de entrada.
        n: Tamanho da lista.
        i: Índice do elemento atual.
    """

    largest = i  # Inicializa o maior elemento como raiz
    left = 2 * i + 1     # Índice do filho à esquerda = 2*i + 1
    right = 2 * i + 2     # Índice do filho à direita = 2*i + 2

    # Veja se o filho da esquerda da raiz existe e é maior que a raiz
    if left < n and arr[i] < arr[left]:
        largest = left

    # Veja se o filho da direita da raiz existe e é maior que a raiz
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Troca e continua o heapify se a raiz não for o maior
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify a raiz.
        heapify(arr, n, largest)

# A função heapify é um componente chave na implementação do algoritmo Heap Sort, que é um algoritmo de ordenação eficiente que utiliza uma estrutura de dados chamada heap. A função heapify transforma uma lista em um heap, que é uma árvore binária completa onde o nó pai é maior (ou menor, dependendo se é um heap máximo ou mínimo) do que seus nós filhos.