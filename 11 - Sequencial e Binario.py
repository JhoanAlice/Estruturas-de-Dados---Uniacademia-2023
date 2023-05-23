# PESQUISA SEQUENCIAL

def scan(alist, key):
    N = len(alist)  # Obtém o tamanho da lista alist
    for i in range(0, N):  # Itera sobre todos os elementos da lista
        if alist[i] == key:  # Se o elemento na posição i é igual à chave, retorna o índice
            return i
        elif key < alist[i]:  # Se a chave é menor que o elemento na posição i, a chave não está na lista
            return -1  # Retorna -1 para indicar que a chave não foi encontrada
    return -1  # Retorna -1 se a chave não foi encontrada após percorrer toda a lista
  
  # PESQUISA BINARIA
  
def iterativeBinarySearch(alist, key):
    N = len(alist)  # Obtém o tamanho da lista alist
    low = 0  # Inicializa a posição de baixo com 0
    high = N - 1  # Inicializa a posição de cima com N - 1

    while low <= high:  # Enquanto a posição de baixo for menor ou igual à posição de cima
        mid = (low + high) // 2  # Calcula a posição do meio
        if alist[mid] == key:  # Se o elemento na posição do meio é igual à chave, retorna o índice
            return mid
        elif key < alist[mid]:  # Se a chave é menor que o elemento na posição do meio, ajusta a posição de cima
            high = mid - 1
        else:  # Se a chave é maior que o elemento na posição do meio, ajusta a posição de baixo
            low = mid + 1
    return -1  # Retorna -1 se a chave não foi encontrada
  
# Atividades
# ● Implemente as pesquisas abaixo:
# A)Pesquisa Sequencial
# B)Pesquisa Binária
# ● Implemente um vetor com 30 números ordenados.
# ● Implemente um mecanismo que possa calcular o tempo de execução
# da pesquisa em sequencial e binária, comparando as duas, em
# termos de tempo gasto. Qual teve melhor desempenho de tempo?
# ● Faça a mesma análise de tempo com uma lista de 30 itens
# desordenada, sendo ordenada pelo bubbleSort e pelo quickSort.
# Qual o tempo melhor entre os 2, para ordenação + pesquisa binária?
  
import random

# Gerando uma lista de 30 números aleatórios entre 1 e 100 e ordenando
lista = sorted([random.randint(1, 100) for _ in range(30)])
print("Lista ordenada de 30 números:", lista)

# Comparação dos tempos de execução da pesquisa sequencial e binária:

import time

key = random.choice(lista)  # Escolhendo um número aleatório da lista como chave

# Teste de tempo para a pesquisa sequencial
start_time = time.time()
index = scan(lista, key)
end_time = time.time()
print(f"A pesquisa sequencial encontrou a chave {key} na posição {index} em {end_time - start_time} segundos.")

# Teste de tempo para a pesquisa binária
start_time = time.time()
index = iterativeBinarySearch(lista, key)
end_time = time.time()
print(f"A pesquisa binária encontrou a chave {key} na posição {index} em {end_time - start_time} segundos.")

# Comparação do tempo de execução para ordenar uma lista desordenada usando Bubble Sort e Quick Sort, seguido de uma pesquisa binária:

def bubble_sort(alist):
    for pass_num in range(len(alist) - 1, 0, -1):
        for i in range(pass_num):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
    return alist

def quick_sort(alist):
    if len(alist) <= 1:
        return alist
    else:
        pivot = alist[0]
        less = [i for i in alist[1:] if i <= pivot]
        greater = [i for i in alist[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


# Gerando uma lista de 30 números aleatórios desordenados entre 1 e 100
desordenada = [random.randint(1, 100) for _ in range(30)]

# Ordenando a lista desordenada usando Bubble Sort e executando a pesquisa binária
start_time = time.time()
ordenada_bubble = bubble_sort(desordenada[:])
index = iterativeBinarySearch(ordenada_bubble, key)
end_time = time.time()
print(f"Bubble Sort e pesquisa binária levaram {end_time - start_time} segundos.")

# Ordenando a lista desordenada usando Quick Sort e executando a pesquisa binária
start_time = time.time()
ordenada_quick = quick_sort(desordenada[:])
index = iterativeBinarySearch(ordenada_quick, key)
end_time = time.time()
print(f"Quick Sort e pesquisa binária levaram {end_time - start_time} segundos.")


# O Quick Sort geralmente tem um desempenho melhor do que o Bubble Sort para listas maiores, devido à sua complexidade de tempo média O(n log n) em comparação com a complexidade de tempo quadrático O(n^2) do Bubble Sort. No entanto, o desempenho exato pode variar dependendo da implementação específica e da distribuição dos dados na lista.
