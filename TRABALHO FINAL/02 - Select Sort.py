from typing import List

def select_sort(arr: List[int]) -> List[int]:
    """
    Esta função implementa o algoritmo Selection Sort.
    Recebe uma lista de inteiros e retorna a lista ordenada.
    """

    # Percorrer todos os elementos da lista
    for i in range(len(arr)):
        # Encontrar o mínimo em arr[i:]
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
                
        # Trocar o mínimo encontrado com o primeiro elemento        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


# Este código implementa o algoritmo Selection Sort. O algoritmo divide a lista de entrada em duas partes: a sublista de itens já classificados, que é construída da esquerda para a direita no início da lista, e a sublista dos itens restantes a serem classificados, que ocupam o resto da lista. Inicialmente, a sublista classificada está vazia e a sublista não classificada é a lista de entrada inteira. O algoritmo prossegue encontrando o menor (ou maior, dependendo da ordem de classificação) elemento na sublista não classificada, trocando-o com o elemento não classificado mais à esquerda (colocando-o em ordem) e movendo os limites da sublista um elemento para a direita.