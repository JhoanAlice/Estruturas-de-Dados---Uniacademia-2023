from typing import List, Optional

def binary_search(arr: List[int], low: int, high: int, target: int) -> Optional[int]:
    """
    Esta função implementa o algoritmo de Pesquisa Binária.
    Ela recebe uma lista (que deve estar ordenada), um intervalo de índices e um alvo,
    e retorna o índice do alvo na lista dentro do intervalo especificado.
    Se o alvo não estiver na lista, retorna None.

    Args:
        arr: A lista de entrada.
        low: O índice inicial do intervalo de busca.
        high: O índice final do intervalo de busca.
        target: O alvo da pesquisa.

    Returns:
        O índice do alvo na lista, ou None se o alvo não estiver na lista.
    """

    if high >= low:

        mid = (high + low) // 2

        # Se o elemento está presente no meio
        if arr[mid] == target:
            return mid

        # Se o elemento é menor que o do meio,
        # então ele só pode estar presente no subarray à esquerda
        elif arr[mid] > target:
            return binary_search(arr, low, mid - 1, target)

        # Caso contrário, o elemento só pode estar no subarray à direita
        else:
            return binary_search(arr, mid + 1, high, target)

    else:
        # O elemento não está presente na lista
        return None

# A pesquisa binária é um algoritmo eficiente para encontrar um item em uma lista ordenada de itens. Ele funciona dividindo repetidamente pela metade a parte da lista que pode conter o item, até reduzir as localizações possíveis a apenas uma.