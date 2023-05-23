# 5. **Quick Sort:** Assim como o Merge Sort, o Quick Sort também é um algoritmo de divisão e conquista. Ele escolhe um elemento como pivô, rearranja a lista de modo que todos os elementos menores que o pivô venham antes e todos os elementos maiores venham depois (isso é chamado de partição), e então ordena as duas sublistas de forma independente. O Quick Sort tem uma complexidade de tempo média de O(n log n), mas no pior caso pode chegar a O(n²).

# Função para trocar os elementos de posição i e j na lista alist
def swap(alist, i, j):  
    temp = alist[i]  # Armazena o valor do elemento na posição i em uma variável temporária
    alist[i] = alist[j]  # Atribui o valor do elemento na posição j à posição i
    alist[j] = temp  # Atribui o valor do elemento temporário à posição j

def quicksort_verbose(alist):
    N = len(alist)

    def recursiveQuickSort(alist, posMin, posMax):
        if posMin < posMax:
            p = partition(alist, posMin, posMax)
            print(f'Particionando: {alist[posMin:posMax + 1]} -> {alist[posMin:p]} (Pivô: {alist[p]}) {alist[p + 1:posMax + 1]}')
            recursiveQuickSort(alist, posMin, p)
            recursiveQuickSort(alist, p + 1, posMax)

    def partition(alist, posMin, posMax):
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
        return j

    print(f'Lista inicial: {alist}')
    recursiveQuickSort(alist, 0, N - 1)
    print(f'Lista ordenada: {alist}')
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
    quicksort_verbose(lista)

# Perguntas:
# 1) Qual a principal regra a ser respeitada pelo particionamento?
# R: A principal regra a ser respeitada pelo particionamento é que todos os elementos menores que o pivô devem ser colocados à esquerda do pivô e todos os elementos maiores devem ser colocados à direita do pivô. 
# Isso garante que o pivô esteja em sua posição correta na lista ordenada, e o processo pode ser aplicado recursivamente nas sub-listas à esquerda e à direita do pivô para ordenar a lista completa.
