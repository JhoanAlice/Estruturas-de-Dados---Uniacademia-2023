def quick_sort_tad(numbers):
    _quick_sort(numbers, 0, len(numbers) - 1)
    return numbers

def _quick_sort(numbers, low, high):
    if low < high:
        pivot_index = partition(numbers, low, high)
        _quick_sort(numbers, low, pivot_index - 1)
        _quick_sort(numbers, pivot_index + 1, high)

def partition(numbers, low, high):
    mid = (low + high) // 2
    pivot = sorted([numbers[low], numbers[mid], numbers[high]])[1]
    pivot_index = numbers.index(pivot)
    numbers[pivot_index], numbers[high] = numbers[high], numbers[pivot_index]
    
    i = low
    for j in range(low, high):
        if numbers[j] <= pivot:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            i = i + 1
    numbers[i], numbers[high] = numbers[high], numbers[i]
    return i
