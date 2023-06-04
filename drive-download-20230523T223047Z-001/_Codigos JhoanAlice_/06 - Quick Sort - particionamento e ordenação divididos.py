# Função para trocar os elementos de posição i e j na lista alist
def swap(alist, i, j):  
    temp = alist[i]  # Armazena o valor do elemento na posição i em uma variável temporária
    alist[i] = alist[j]  # Atribui o valor do elemento na posição j à posição i
    alist[j] = temp  # Atribui o valor do elemento temporário à posição j

def partition_verbose(alist, posMin, posMax):
    pivot = alist[posMin]
    i = posMin + 1
    j = posMax

    while True:
        while i < posMax and alist[i] <= pivot:
            i = i + 1
        while j > posMin and alist[j] >= pivot:
            j = j - 1
        if i < j:
            swap(alist, i, j)
        else:
            break

    swap(alist, posMin, j)
    print(f'Particionando: {alist[posMin:posMax + 1]} -> {alist[posMin:j]} (Pivô: {alist[j]}) {alist[j + 1:posMax + 1]}')
    return j

def recursive_quick_sort_verbose(alist, posMin, posMax):
    if posMin < posMax:
        p = partition_verbose(alist, posMin, posMax)
        recursive_quick_sort_verbose(alist, posMin, p - 1)
        recursive_quick_sort_verbose(alist, p + 1, posMax)

    return alist

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
    recursive_quick_sort_verbose(lista, 0, len(lista) - 1)
    print('Lista ordenada:', lista)
# 1 - Qual a principal regra a ser respeitada pelo particionamento?
# R: A principal regra a ser respeitada pelo particionamento é que todos os elementos menores que o pivô devem ser colocados à esquerda do pivô e todos os elementos maiores devem ser colocados à direita do pivô. Isso garante que o pivô esteja em sua posição correta na lista ordenada, e o processo pode ser aplicado recursivamente nas sub-listas à esquerda e à direita do pivô para ordenar a lista completa.