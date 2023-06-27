def heap_sort(numbers):
    n = len(numbers)

    for i in range(n//2 - 1, -1, -1):
        heapify(numbers, n, i)

    for i in range(n-1, 0, -1):
        numbers[i], numbers[0] = numbers[0], numbers[i]
        heapify(numbers, i, 0)

    return numbers


def heapify(numbers, heap_size, root_index):
    largest = root_index
    left = 2 * root_index + 1
    right = 2 * root_index + 2

    if left < heap_size and numbers[left] > numbers[largest]:
        largest = left

    if right < heap_size and numbers[right] > numbers[largest]:
        largest = right

    if largest != root_index:
        numbers[root_index], numbers[largest] = numbers[largest], numbers[root_index]
        heapify(numbers, heap_size, largest)
