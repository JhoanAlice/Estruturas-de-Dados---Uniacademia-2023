from typing import List

def insert_sort(arr: List[int]) -> List[int]:
    """
    Esta função implementa o algoritmo Insertion Sort.
    Recebe uma lista de inteiros e retorna a lista ordenada.
    """

    # Percorrer de 1 a len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Mover os elementos de arr[0..i-1], que são maiores que key,
        # para uma posição à frente de sua posição atual
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

    return arr


# Este código implementa o algoritmo Insertion Sort. A ideia por trás do Insertion Sort é que ele divide a lista em uma parte ordenada à esquerda e uma parte não ordenada à direita. Em seguida, pega iterativamente o primeiro elemento não ordenado (chamado de "chave") e insere-o no local correto na parte ordenada da lista.