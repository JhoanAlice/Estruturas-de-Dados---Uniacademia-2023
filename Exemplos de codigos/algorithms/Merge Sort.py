from typing import List

def merge_sort(arr: List[int]) -> List[int]:
    """
    Esta função implementa o algoritmo Merge Sort.
    Recebe uma lista de inteiros e retorna a lista ordenada.
    """

    if len(arr) <= 1:
        return arr

    # Encontre o meio da lista
    mid = len(arr) // 2

    # Divida a lista em duas metades
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Chame merge_sort recursivamente para cada metade
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Combine as duas metades ordenadas
    return merge(left_half, right_half)

def merge(left: List[int], right: List[int]) -> List[int]:
    """
    Esta função é uma subfunção do Merge Sort.
    Ela combina duas listas ordenadas em uma nova lista ordenada.
    """

    merged = []
    left_index = 0
    right_index = 0

    # Loop até que todos os elementos sejam adicionados à lista merged
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Adicione os elementos restantes, se houver
    if left_index < len(left):
        merged.extend(left[left_index:])
    elif right_index < len(right):
        merged.extend(right[right_index:])

    return merged

# Este código implementa o algoritmo Merge Sort. O Merge Sort é um algoritmo de classificação dividir para conquistar. Ele divide a lista de entrada em duas metades, chama a si mesmo para as duas metades e, em seguida, mescla as duas listas ordenadas. A função merge() é usada para mesclar duas listas.