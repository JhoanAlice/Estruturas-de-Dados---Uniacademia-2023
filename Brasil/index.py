import heapq
import time
from typing import List

import pandas as pd

# 1. Ler a planilha
df = pd.read_excel('planilha.xlsx')
cidades = df['Nome_Município'].tolist()
estados = df['Nome Região Geográfica Imediata'].tolist()
distritos = df['Nome_Distrito'].tolist()


# Criar uma lista de tuplas (cidade, estado)
lista = list(zip(cidades, estados))

# Implementação de Algorítimos de busca


def sequential_search(arr: List, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr: List, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# Implementação dos algoritmos de ordenação

def bubble_sort(arr: List):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr: List):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr: List):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr: List):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        return quick_sort([x for x in arr[1:] if x < arr[0]]) + [arr[0]] + quick_sort([x for x in arr[1:] if x >= arr[0]])


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


# Funções para ordenar e buscar

# Ordenar estados por ordem alfabética
def ordenar_estados(estados, algoritmo):
    start_time = time.time()
    estados_ordenados = algoritmo(estados)
    end_time = time.time()
    return estados_ordenados, end_time - start_time


# Ordenar distritos por ordem alfabética
def ordenar_distritos(distritos, algoritmo):
    start_time = time.time()
    distritos_ordenados = algoritmo(distritos)
    end_time = time.time()
    return distritos_ordenados, end_time - start_time

# Ordenar as cidades de um estado específico por ordem alfabética


def ordenar_cidades_estado(lista, estado, algoritmo):
    start_time = time.time()
    cidades_estado = [cidade for cidade,
                      estado_lista in lista if estado_lista == estado]
    cidades_ordenadas = algoritmo(cidades_estado)
    end_time = time.time()
    return cidades_ordenadas, end_time - start_time

# Ordenar todas as cidades por ordem alfabética


def ordenar_todas_cidades(lista, algoritmo):
    start_time = time.time()
    cidades = [cidade for cidade, estado in lista]
    cidades_ordenadas = algoritmo(cidades)
    end_time = time.time()
    return cidades_ordenadas, end_time - start_time

# Ordenar os distritos de uma cidade por ordem alfabética


def ordenar_distritos_cidade(lista, cidade, algoritmo):
    start_time = time.time()
    distritos_cidade = [distrito for distrito,
                        cidade_lista in lista if cidade_lista == cidade]
    distritos_ordenados = algoritmo(distritos_cidade)
    end_time = time.time()
    return distritos_ordenados, end_time - start_time

# Ordenar os distritos de um estado por ordem alfabética


def ordenar_distritos_estado(lista, estado, algoritmo):
    start_time = time.time()
    distritos_estado = [distrito for distrito,
                        estado_lista in lista if estado_lista == estado]
    distritos_ordenados = algoritmo(distritos_estado)
    end_time = time.time()
    return distritos_ordenados, end_time - start_time

# Buscar e listar as cidades que iniciam com as letras escolhidas por estado


def buscar_cidades_iniciais_estado(lista, letras, estado):
    cidades_estado = [cidade for cidade, estado_lista in lista if estado_lista ==
                      estado and cidade.startswith(letras)]
    return cidades_estado

# Buscar e listar os distritos que iniciam com as letras escolhidas por estado


def buscar_distritos_iniciais_estado(lista, letras, estado):
    distritos_estado = [distrito for distrito,
                        estado_lista in lista if estado_lista == estado and distrito.startswith(letras)]
    return distritos_estado

# Buscar e listar as cidades que iniciam com as letras escolhidas em todos os estados


def buscar_cidades_iniciais_todos_estados(lista, letras):
    cidades = [cidade for cidade,
               estados in lista if cidade.startswith(letras)]
    return cidades

# Buscar e listar os distritos que iniciam com as letras escolhidas em todos os estados


def buscar_distritos_iniciais_todos_estados(lista, letras):
    distritos = [distrito for distrito,
                 estados in lista if distrito.startswith(letras)]
    return distritos

# Inserção de arvores


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


def search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)


# 3. Interface do usuário
while True:
    print("\n1. Ordenar todos os estados")
    print("2. Ordenar todas as cidades")
    print("3. Ordenar todas os distritos")
    print("4. Ordenar cidades de um estado")
    print("5. Ordenar distritos de uma cidade")
    print("6. Ordenar distritos de um estado")
    print("7. Buscar cidades que iniciam com certas letras em um estado")
    print("8. Buscar distritos que iniciam com certas letras em um estado")
    print("9. Buscar cidades que iniciam com certas letras em todos os estados")
    print("10. Buscar distritos que iniciam com certas letras em todos os estados")
    print("11. Buscar estado (busca sequencial)")
    print("12. Buscar distrito (busca sequencial)")
    print("13. Buscar estado (busca binária)")
    print("14. Buscar distrito (busca binária)")
    #
    print("15. Inserir item na árvore")
    print("16. Buscar item na árvore")
    print("17. Imprimir todos os itens na árvore")
    #
    print("18. Sair")

    opcao = input("\nEscolha uma opção: ")
    ##### Metodos de ordenação #####
    ##### Metodos de ordenação #####
    if opcao in ['1', '2', '3', '4', '5', '6']:
        print("\n1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Insertion Sort")
        print("4. Merge Sort")
        print("5. Quick Sort")
        print("6. Heap Sort")
        algoritmo_opcao = input("\nEscolha um algoritmo de ordenação: ")
        algoritmo = None
        algoritmo_escolhido = None
        busca_escolhida = None
        if algoritmo_opcao == '1':
            algoritmo = bubble_sort
            algoritmo_escolhido = "Bubble Sort"
        elif algoritmo_opcao == '2':
            algoritmo = selection_sort
            algoritmo_escolhido = "Selection Sort"
        elif algoritmo_opcao == '3':
            algoritmo = insertion_sort
            algoritmo_escolhido = "Insertion Sort"
        elif algoritmo_opcao == '4':
            algoritmo = merge_sort
            algoritmo_escolhido = "Merge Sort"
        elif algoritmo_opcao == '5':
            algoritmo = quick_sort
            algoritmo_escolhido = "Quick Sort"
        elif algoritmo_opcao == '6':
            algoritmo = heap_sort
            algoritmo_escolhido = "Heap Sort"
        else:
            print("Opção inválida. Tente novamente.")
            continue
    ##### Comparações #####
    ##### Comparações #####
    if opcao == '1':
        estados_ordenados, tempo = ordenar_estados(estados, quick_sort)
        print(f"Estados ordenados: {estados_ordenados}")
        print(
            f"Utilizando o método Quick Sort, o tempo de ordenação foi: {tempo} segundos")
    ###
    ###
    elif opcao == '2':
        cidades_ordenadas, tempo = ordenar_todas_cidades(lista, algoritmo)
        print(f"Cidades ordenadas: {cidades_ordenadas}")
        print(
            f"Utilizando o método {algoritmo_escolhido}, o tempo de ordenação foi: {tempo} segundos")
    ###
    ###
    elif opcao == '3':
        distritos_ordenados, tempo = ordenar_distritos(lista, algoritmo)
        print(f"Distritos ordenados: {distritos_ordenados}")
        print(
            f"Utilizando o método {algoritmo_escolhido}, o tempo de ordenação foi: {tempo} segundos")
    ###
    ###
    elif opcao == '4':
        estado = input("Digite o estado: ")
        cidades_ordenadas, tempo = ordenar_cidades_estado(
            lista, estado, algoritmo)
        print(f"Cidades ordenadas: {cidades_ordenadas}")
        print(
            f"Utilizando o método {algoritmo_escolhido}, o tempo de ordenação foi: {tempo} segundos")
    ###
    ###
    elif opcao == '5':
        cidade = input("Digite a cidade: ")
        distritos_ordenados, tempo = ordenar_distritos_cidade(
            lista, cidade, algoritmo)
        print(f"Distritos ordenados: {distritos_ordenados}")
        print(
            f"Utilizando o método {algoritmo_escolhido}, o tempo de ordenação foi: {tempo} segundos")
    ###
    ###
    elif opcao == '6':
        estado = input("Digite o estado: ")
        distritos_ordenados, tempo = ordenar_distritos_cidade(
            lista, estado, algoritmo)
        print(f"Distritos ordenados: {distritos_ordenados}")
        print(
            f"Utilizando o método {algoritmo_escolhido}, o tempo de ordenação foi: {tempo} segundos")
    ###
    ###
    elif opcao == '7':
        letras = input("Digite as letras iniciais: ")
        estado = input("Digite o estado: ")
        print(buscar_cidades_iniciais_estado(lista, letras, estado))
        print(
            f"Aqui está uma lista de cidades que iniciam com a letra {letras} no estado de {estado}")
    ###
    ###
    elif opcao == '8':
        letras = input("Digite as letras iniciais: ")
        estado = input("Digite o estado: ")
        print(buscar_distritos_iniciais_estado(lista, letras, estado))
        print(
            f"Aqui está uma lista de distritos que iniciam com a letra {letras} no estado de {estado}")
    ###
    ###
    elif opcao == '9':
        letras = input("Digite as letras iniciais: ")
        print(buscar_cidades_iniciais_todos_estados(lista, letras))
        print(
            f"Aqui está uma lista de cidades que iniciam com a letra {letras} em todos os estados do país")
    ###
    ###
    elif opcao == '10':
        letras = input("Digite as letras iniciais: ")
        print(buscar_distritos_iniciais_todos_estados(lista, letras))
        print(
            f"Aqui está uma lista de distritos que iniciam com a letra {letras} em todos os estados do país")
    ##### Buscas#####
    ##### Buscas#####
    elif opcao == '11':
        busca_escolhida = "Busca Sequencial"
        estado = input("Digite o estado a ser buscado: ")
        start_time = time.time()
        index = sequential_search(estados, estado)
        end_time = time.time()
        if index != -1:
            print(f"Estado {estado} encontrado no índice {index}")
        else:
            print(f"Estado {estado} não encontrado")
        print(f"Tempo de busca: {end_time - start_time} segundos")
    ###
    ###
    elif opcao == '12':
        busca_escolhida = "Busca Sequencial"
        distrito = input("Digite o distrito a ser buscado: ")
        start_time = time.time()
        index = sequential_search(distritos, distrito)
        end_time = time.time()
        if index != -1:
            print(f"Distrito {distrito} encontrado no índice {index}")
        else:
            print(f"Distrito {distrito} não encontrado")
        print(f"Tempo de busca: {end_time - start_time} segundos")
    ###
    ###
    elif opcao == '13':
        busca_escolhida = "Busca Binária"
        estado = input("Digite o estado a ser buscado: ")
        start_time = time.time()
        index = binary_search(estados, estado)
        end_time = time.time()
        if index != -1:
            print(f"Estado {estado} encontrado no índice {index}")
        else:
            print(f"Estado {estado} não encontrado")
        print(f"Tempo de busca: {end_time - start_time} segundos")
    ###
    ###
    elif opcao == '14':
        busca_escolhida = "Busca Binária"
        distrito = input("Digite o distrito a ser buscado: ")
        start_time = time.time()
        index = binary_search(distritos, distrito)
        end_time = time.time()
        if index != -1:
            print(f"Distrito {distrito} encontrado no índice {index}")
        else:
            print(f"Distrito {distrito} não encontrado")
        print(f"Tempo de busca: {end_time - start_time} segundos")

        while True:
            opcao = input("Digite a opção desejada: ")

    elif opcao == '15':
        root = None
        item = input("Digite o item a ser inserido: ")
        root = insert(root, item)
    elif opcao == '16':
        root = None
        item = input("Digite o item a ser buscado: ")
        result = search(root, item)
        if result:
            print("Item encontrado")
        else:
            print("Item não encontrado")
    elif opcao == '17':
        root = None
        print("Itens na árvore:")
        inorder(root)
    elif opcao == '18':
        break
    else:
        print("Opção inválida. Tente novamente.")
