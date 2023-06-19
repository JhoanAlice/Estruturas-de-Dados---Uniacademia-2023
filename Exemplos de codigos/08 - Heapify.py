# 8. **Heap Sort (Heapify):** Heapify é um processo de construção de um Heap a partir de um determinado array, o qual é um passo fundamental do algoritmo Heap Sort. Este algoritmo transforma a lista em um Heap, e então extrai o maior elemento (a raiz do Heap) várias vezes até que o Heap esteja vazio, resultando em uma lista ordenada. A complexidade de tempo do Heap Sort é O(n log n).


# Função para garantir a propriedade de max heap (pai é maior que os filhos)
def heapify(arr, n, i):
    largest = i  # Inicializar o maior como raiz
    left = 2 * i + 1  # Índice do filho à esquerda = 2 * i + 1
    right = 2 * i + 2  # Índice do filho à direita = 2 * i + 2

    # Verificar se o filho da esquerda existe e é maior que a raiz
    if left < n and arr[i] < arr[left]:
        largest = left

    # Verificar se o filho da direita existe e é maior que a raiz
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Trocar a raiz, se necessário
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        print("Troca:", arr)  # Mostrar o estado atual do array após trocar os elementos

        # Continuar garantindo a propriedade de max heap para a raiz novamente.
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    # Construir o max heap.
    # Como o último nó pai estará em ((n//2)-1), podemos começar nesse local.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    print("Max Heap construído:", arr)  # Mostrar o estado do array após construir o max heap

    # Um por um extrai elementos
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Trocar
        print("Extraindo elemento:", arr)  # Mostrar o estado do array após extrair o elemento
        heapify(arr, i, 0)

# Listas a serem ordenadas
A = [2, 5, 9, 22, 1]
B = [1, 2, 5, 9, 22]
C = [22, 9, 5, 2, 1]
D = [22, 9, 1, 2, 5]

print("Ordenando lista A:")
heapSort(A)
print("Lista A ordenada:", A)

print("\nOrdenando lista B:")
heapSort(B)
print("Lista B ordenada:", B)

print("\nOrdenando lista C:")
heapSort(C)
print("Lista C ordenada:", C)

print("\nOrdenando lista D:")
heapSort(D)
print("Lista D ordenada:", D)

# 1) Qual a importância do heapify?
# A importância da função heapify reside na manutenção da propriedade de heap, que é crucial para o funcionamento do Heap Sort. A propriedade de heap é a condição que mantém o maior elemento na raiz do heap, permitindo sua remoção e reposicionamento para a ordenação. A função heapify também é responsável por reestruturar o heap após a remoção do maior elemento, garantindo que o próximo maior elemento seja colocado na raiz. Isso é repetido até que todos os elementos sejam removidos e ordenados.