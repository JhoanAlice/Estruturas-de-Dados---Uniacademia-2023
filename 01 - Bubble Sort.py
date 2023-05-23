# 1. **Bubble Sort:** Este é um algoritmo simples que percorre repetidamente a lista, troca elementos adjacentes se estiverem na ordem errada e continua o processo até que não haja mais trocas necessárias. Sua principal desvantagem é a ineficiência para listas maiores, pois tem uma complexidade de tempo O(n²).

# Função para trocar dois elementos de posição em uma lista
def swap(alist, i, j):
    # Guarda o valor de alist[i] em uma variável temporária
    temp = alist[i]
    # Substitui o valor de alist[i] pelo valor de alist[j]
    alist[i] = alist[j]
    # Substitui o valor de alist[j] pelo valor temporário guardado
    alist[j] = temp

# Função para ordenar uma lista usando o algoritmo Bubble Sort
def BubbleSort(alist):
    # Obtém o tamanho da lista
    N = len(alist)
    # Percorre a lista N-1 vezes
    for passnum in range(1, N):
        # Percorre a lista da posição 0 até a posição N-passnum
        for i in range(0, N-passnum):
            # Verifica se o elemento atual é maior que o próximo elemento
            if alist[i] > alist[i+1]:
                # Troca os elementos de posição
                swap(alist, i, i+1)
    # Retorna a lista ordenada
    return alist
#Atividades
#● Implemente o método bubble sort para ordenar as listas abaixo:
#A) [2,5,9,22,1]
#B) [1,2,5,9,22]
#C) [22,9,5,2,1]
#D) [22,9,1,2,5]

#● Faça prints para mostrar como as listas foram ordenadas.
#● Responda as perguntas:

#1) Qual das listas usou todos os caminhos do algoritmo
#BubbleSort?

#2) Qual das listas menos usou o algoritmo para ordenação?

# Listas para teste
listas = [
    [2, 5, 9, 22, 1],
    [1, 2, 5, 9, 22],
    [22, 9, 5, 2, 1],
    [22, 9, 1, 2, 5]
]

# Ordenação das listas utilizando Bubble Sort
for lista in listas:
    print("Lista original:", lista)
    print("Ordenando a lista:")
    BubbleSort(lista)
    print("Lista ordenada:", lista)
    print()

# Perguntas:
# 1) Qual das listas usou todos os caminhos do algoritmo Bubble Sort?
# R: A lista [22, 9, 5, 2, 1] usou todos os caminhos do algoritmo Bubble Sort,
# pois estava completamente desordenada e todos os elementos precisaram ser movidos.

# 2) Qual das listas menos usou o algoritmo para ordenação?
# R: A lista [1, 2, 5, 9, 22] é a que menos usou o algoritmo para ordenação,
# pois já estava ordenada e nenhuma troca foi necessária.
