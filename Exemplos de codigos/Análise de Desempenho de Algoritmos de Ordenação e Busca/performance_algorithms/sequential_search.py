def sequential_search(numbers, target):
    for i, number in enumerate(numbers):
        if number == target:
            return i
    return -1
