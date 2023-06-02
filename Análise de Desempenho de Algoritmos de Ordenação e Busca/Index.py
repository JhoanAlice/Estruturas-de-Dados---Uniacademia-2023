import time
from performance_algorithms import bubble_sort
from performance_algorithms import select_sort
from performance_algorithms import insert_sort
from performance_algorithms import merge_sort
from performance_algorithms import quick_sort
from performance_algorithms import quick_sort_tad
from performance_algorithms import heap_sort
from performance_algorithms import sequential_search
from performance_algorithms import binary_search

def read_file(filename):
    with open(filename, 'r') as file:
        content = [int(x) for x in file.read().split()]
    return content

def measure_execution_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return end_time - start_time


def main():
    filenames = [
        ("small_data.txt", "Small Data"),
        ("large_data.txt", "Large Data"),
        ("sorted_data.txt", "Sorted Data"),
        ("reversed_data.txt", "Reversed Data"),
    ]

    sort_algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Select Sort", select_sort),
        ("Insert Sort", insert_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
        ("Quick Sort TAD", quick_sort_tad),
        ("Heap Sort", heap_sort),
    ]

    search_algorithms = [
        ("Sequential search", sequential_search),
        ("Binary search", binary_search),
    ]

    for filename, description in filenames:
        print(f"\n{description}:")

        data = read_file(filename)

        for sort_name, sort_func in sort_algorithms:
            sort_time = measure_execution_time(sort_func, data.copy())
            print(f"{sort_name} time: {sort_time:.5f} seconds")

        sorted_data = sorted(data)

        for search_name, search_func in search_algorithms:
            search_time = measure_execution_time(search_func, sorted_data, sorted_data[-1])
            print(f"{search_name} time: {search_time:.5f} seconds")


if __name__ == "__main__":
    main()
