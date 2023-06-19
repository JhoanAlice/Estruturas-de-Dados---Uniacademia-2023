from typing import List, Optional

def sequential_search(arr: List[int], target: int) -> Optional[int]:
    """
    Esta função implementa o algoritmo de Pesquisa Sequencial.
    Ela recebe uma lista e um alvo, e retorna o índice do alvo na lista.
    Se o alvo não estiver na lista, retorna None.

    Args:
        arr: A lista de entrada.
        target: O alvo da pesquisa.

    Returns:
        O índice do alvo na lista, ou None se o alvo não estiver na lista.
    """

    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Retorna o índice do alvo

    return None  # O alvo não está na lista

# A pesquisa sequencial é um método simples para encontrar um elemento específico em uma lista. Ele verifica cada elemento da lista em sequência até encontrar um elemento que corresponda ao alvo. Se o elemento for encontrado, a função retorna o índice do elemento na lista. Se o elemento não for encontrado, a função retorna None.




