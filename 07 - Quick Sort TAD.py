# Função para trocar elementos de posição i e j na lista alist
def swap(alist, i, j):
    temp = alist[i]  # Armazenar temporariamente o valor na posição i
    alist[i] = alist[j]  # Atribuir o valor da posição j à posição i
    alist[j] = temp  # Atribuir o valor temporário à posição j

def quicksort_verbose(alist):
    N = len(alist)  # Pegar o tamanho da lista alist

    def partition_verbose(alist, posMin, posMax):
        pivot = alist[posMin]  # Escolher o primeiro elemento da lista como pivô
        i = posMin + 1  # Iniciar i no segundo elemento da lista
        j = posMax  # Iniciar j no último elemento da lista

        while True:
            while i < posMax and alist[i] <= pivot:  # Encontrar o primeiro elemento maior que o pivô
                i = i + 1
            while j > posMin and alist[j] >= pivot:  # Encontrar o primeiro elemento menor que o pivô
                j = j - 1
            if i < j:  # Verificar se i e j ainda não cruzaram
                swap(alist, i, j)  # Trocar os elementos encontrados
            else:
                break  # Parar o loop se i e j cruzarem

        swap(alist, posMin, j)  # Trocar o pivô com o elemento na posição j
        print(f'Particionando: {alist[posMin:posMax + 1]} -> {alist[posMin:j]} (Pivô: {alist[j]}) {alist[j + 1:posMax + 1]}')
        return j  # Retornar o índice do pivô

    def recursive_quick_sort_verbose(alist, posMin, posMax):
        if posMin < posMax:  # Verificar se a lista tem mais de um elemento
            p = partition_verbose(alist, posMin, posMax)  # Particionar a lista e pegar o índice do pivô
            recursive_quick_sort_verbose(alist, posMin, p)  # Chamar a função recursivamente para a sublista à esquerda do pivô
            recursive_quick_sort_verbose(alist, p + 1, posMax)  # Chamar a função recursivamente para a sublista à direita do pivô

    recursive_quick_sort_verbose(alist, 0, N - 1)  # Chamar a função recursiva com o índice inicial e final da lista
    return alist  # Retornar a lista ordenada

# Ordenando as listas fornecidas
listas = [
    [2, 5, 9, 22, 1],
    [1, 2, 5, 9, 22],
    [22, 9, 5, 2, 1],
    [22, 9, 1, 2, 5]
]

for lista in listas:
    print('\nOrdenando a lista:')
    print('Lista inicial:', lista)
    quicksort_verbose(lista)
    print('Lista ordenada:', lista)
