# Função para mesclar duas sublistas ordenadas
def merge(lado_esq, lado_dir):
    # Cria uma lista vazia para armazenar o resultado
    resultado = []
    
    # Enquanto ambas as sublistas não estiverem vazias
    while lado_esq and lado_dir:
        # Se o primeiro elemento da sublista esquerda for menor
        if lado_esq[0] < lado_dir[0]:
            # Adiciona o primeiro elemento da sublista esquerda ao resultado e remove-o da sublista esquerda
            resultado.append(lado_esq.pop(0))
        else:
            # Adiciona o primeiro elemento da sublista direita ao resultado e remove-o da sublista direita
            resultado.append(lado_dir.pop(0))
    
    # Adiciona os elementos restantes das sublistas (caso ainda existam)
    resultado.extend(lado_esq)
    resultado.extend(lado_dir)
    
    return resultado


# Função para ordenar uma lista usando o algoritmo Merge Sort
def mergeSort(alist):
    N = len(alist)

    # Caso base: se a lista tiver apenas um elemento, retorna a própria lista
    if len(alist) <= 1:
        return alist

    # Divide a lista em duas metades
    mid = N // 2
    lado_esq = alist[:mid]
    lado_dir = alist[mid:]

    # Ordena recursivamente as duas metades
    lado_esq = mergeSort(lado_esq)
    lado_dir = mergeSort(lado_dir)

    # Mescla as duas metades ordenadas
    alist = merge(lado_esq, lado_dir)

    return alist

# Listas para teste
listas = [
    [2, 5, 9, 22, 1],
    [1, 2, 5, 9, 22],
    [22, 9, 5, 2, 1],
    [22, 9, 1, 2, 5]
]

# Ordenação das listas utilizando Merge Sort
for lista in listas:
    print("Lista original:", lista)
    lista_ordenada = mergeSort(lista)
    print("Lista ordenada:", lista_ordenada)

# Perguntas:
# 1) Porque o merge sort trabalha conceitos de lado direito e lado esquerdo?
# R: O Merge Sort trabalha com os conceitos de lado direito e lado esquerdo porque é um algoritmo de ordenação que utiliza a técnica de divisão e conquista. 
# A ideia é dividir a lista em duas metades e resolver o problema de ordenação em cada metade de forma independente e recursiva. 
# Após ordenar as metades, o algoritmo mescla (merge) as duas metades ordenadas em uma única lista ordenada.
