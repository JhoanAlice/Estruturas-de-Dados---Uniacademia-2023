from typing import List, Optional

def binary_search(arr: List[int], target: int) -> Optional[int]:
    """
    Implementa o algoritmo de Pesquisa Binária.
    Recebe uma lista e um alvo, e retorna o índice do alvo na lista.
    Se o alvo não estiver na lista, retorna None.
    """

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return None  # O alvo não está na lista


# A pesquisa binária é um algoritmo eficiente para encontrar um item em uma lista ordenada de itens. Ele funciona dividindo repetidamente pela metade a parte da lista que pode conter o item, até reduzir as localizações possíveis a apenas uma.