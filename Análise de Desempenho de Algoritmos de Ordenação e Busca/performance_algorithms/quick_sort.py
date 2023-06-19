def quick_sort(arr):
    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = _partition(arr, low, high)
            if low < pivot_index - 1:
                stack.append((low, pivot_index - 1))
            if pivot_index + 1 < high:
                stack.append((pivot_index + 1, high))

def _partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high

    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    
    arr[low], arr[right] = arr[right], arr[low]
    return right
