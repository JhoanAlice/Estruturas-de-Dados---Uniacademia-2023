# Função para trocar dois elementos de posição em uma lista (não será usada neste exemplo)
def swap(alist, i, j):
    # Guarda o valor de alist[i] em uma variável temporária
    temp = alist[i]
    # Substitui o valor de alist[i] pelo valor de alist[j]
    alist[i] = alist[j]
    # Substitui o valor de alist[j] pelo valor temporário guardado
    alist[j] = temp

# Função para ordenar uma lista usando o algoritmo de Ordenação por Inserção
def insertSort(alist):
    # Obtém o tamanho da lista
    N = len(alist)
    # Percorre a lista da posição 1 até a posição N-1
    for i in range(1, N):
        # Guarda o valor do elemento na posição i
        aux = alist[i]
        # Inicializa j como i-1
        j = i-1
        # Percorre a lista da posição j até a posição 0, enquanto o elemento na posição j for maior que aux
        while j >= 0 and alist[j] > aux:
            # Move o elemento na posição j para a posição j+1
            alist[j+1] = alist[j]
            # Decrementa j
            j = j-1
        # Insere aux na posição j+1
        alist[j+1] = aux
    # Retorna a lista ordenada
    return alist

# Definição da lista exemplo
exemplo = [22, 9, 5, 2, 1]

# Ordenando a lista com insertSort
print("Lista ordenada:", insertSort(exemplo))

# Atividades
# Responda:
# – Mostre como ficaria o vetor resultante enquanto:
# ● I = 3, j=2
# – Mostre o valor de i e j quando aux == 22
# – Mostre o vetor resultante quando j= 0 pela segunda vez.

# Respostas

# Para responder à pergunta 1, vamos executar o insertSort até i = 3, j = 2
i = 3
exemplo = [22, 9, 5, 2, 1]
aux = exemplo[i]
j = i - 1
while j >= 0 and exemplo[j] > aux:
    exemplo[j + 1] = exemplo[j]
    j = j - 1
exemplo[j + 1] = aux
print("Vetor resultante enquanto i = 3, j = 2:", exemplo)

# Para responder à pergunta 2, vamos encontrar os valores de i e j quando aux == 22
exemplo = [22, 9, 5, 2, 1]
i = -1
j = -1
for indice in range(len(exemplo)):
    if exemplo[indice] == 22:
        i = indice
        j = i - 1
        break
print("Valor de i e j quando aux == 22: i =", i, ", j =", j)

# Para responder à pergunta 3, vamos executar o insertSort até que j = 0 pela segunda vez
exemplo = [22, 9, 5, 2,1]
j_zero_count = 0

for i in range(1, len(exemplo)):
    aux = exemplo[i]
    j = i - 1
    while j >= 0 and exemplo[j] > aux:
        if j == 0:
            j_zero_count += 1
        if j_zero_count == 2:
            break
        exemplo[j + 1] = exemplo[j]
        j = j - 1
    if j_zero_count == 2:
        break
    exemplo[j + 1] = aux

print("Vetor resultante quando j = 0 pela segunda vez:", exemplo)
 
