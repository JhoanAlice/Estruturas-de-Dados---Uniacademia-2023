from typing import List

def quick_sort(arr: List[int]) -> List[int]:
    """
    Esta função implementa o algoritmo Quick Sort.
    Recebe uma lista de inteiros e retorna a lista ordenada.
    """

    # Se a lista tem no máximo um elemento, ela já está ordenada
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Este código implementa o algoritmo Quick Sort, que é um algoritmo de classificação dividir para conquistar, como o Merge Sort. A chave do Quick Sort é o elemento de pivô que é usado para a partição. Os elementos são reorganizados de forma que todos os elementos antes do pivô sejam menores que o pivô e todos os elementos após o pivô sejam maiores que o pivô. Em seguida, o algoritmo Quick Sort é aplicado recursivamente às duas subpartes.