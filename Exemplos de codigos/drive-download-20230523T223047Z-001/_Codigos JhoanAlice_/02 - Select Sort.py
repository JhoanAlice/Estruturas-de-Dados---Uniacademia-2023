# Função para trocar dois elementos de posição em uma lista
def swap(alist, i, j):
    # Guarda o valor de alist[i] em uma variável temporária
    temp = alist[i]
    # Substitui o valor de alist[i] pelo valor de alist[j]
    alist[i] = alist[j]
    # Substitui o valor de alist[j] pelo valor temporário guardado
    alist[j] = temp

# Função para ordenar uma lista usando o algoritmo Selection Sort
def selectSort(alist):
    # Obtém o tamanho da lista
    N = len(alist)
    # Percorre a lista da posição 0 até a posição N-1
    for i in range(N-1):
        # Inicializa a posição do mínimo com o índice atual
        positionOfMin = i
        # Percorre a lista da posição i+1 até a posição N
        for j in range(i+1, N):
            # Verifica se o elemento na posição j é menor que o elemento na posição do mínimo
            if alist[j] < alist[positionOfMin]:
                # Atualiza a posição do mínimo
                positionOfMin = j
        # Troca o elemento na posição i com o elemento na posição do mínimo
        swap(alist, i, positionOfMin)
    # Retorna a lista ordenada
    return alist

#Atividades
#● Implemente o método select sort para ordenar as listas abaixo:
#A) [2,5,9,22,1]
#B) [1,2,5,9,22]
#C) [22,9,5,2,1]
#D) [22,9,1,2,5]

#● Faça prints para mostrar como as listas foram ordenadas.
#● Responda as perguntas:

#1) Qual das listas usou todos os caminhos do algoritmo Select
#Sort?

#2) Qual das listas menos usou o algoritmo para ordenação?

# Listas para teste
listas = [
    [2, 5, 9, 22, 1],
    [1, 2, 5, 9, 22],
    [22, 9, 5, 2, 1],
    [22, 9, 1, 2, 5]
]

# Ordenação das listas utilizando Selection Sort
for lista in listas:
    print("Lista original:", lista)
    print("Ordenando a lista:")
    selectSort(lista)
    print("Lista ordenada:", lista)
    print()

# Perguntas:
# 1) Qual das listas usou todos os caminhos do algoritmo Select Sort?
# R: A lista [22, 9, 5, 2, 1] usou todos os caminhos do algoritmo Select Sort,
# pois estava completamente desordenada e todos os elementos precisaram ser movidos.

# 2) Qual das listas menos usou o algoritmo para ordenação?
# R: A lista [1, 2, 5, 9, 22] é a que menos usou o algoritmo para ordenação,
# pois já estava ordenada e nenhuma troca foi necessária.
