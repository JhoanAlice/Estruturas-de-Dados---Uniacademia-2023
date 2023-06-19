import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from performance_algorithms import bubble_sort, select_sort, insert_sort, merge_sort
from performance_algorithms import quick_sort, quick_sort_tad, heap_sort
from performance_algorithms import sequential_search, binary_search, measure_execution_time, read_file
from performance_algorithms import adicionar_a_lista, remover_da_lista, procurar_na_lista
from performance_algorithms import adicionar_a_pilha, remover_da_pilha
from performance_algorithms import adicionar_a_fila, remover_da_fila


def main():
    filenames = [
        ("small_data.txt", "Dados Pequenos"),
        ("large_data.txt", "Dados Grandes"),
        ("sorted_data.txt", "Dados Ordenados"),
        ("reversed_data.txt", "Dados Invertidos"),
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
        ("Busca Sequencial", sequential_search),
        ("Busca Binária", binary_search),
    ]

    data_structures = [
        ("Lista", [adicionar_a_lista, remover_da_lista, procurar_na_lista]),
        ("Pilha", [adicionar_a_pilha, remover_da_pilha]),
        ("Fila", [adicionar_a_fila, remover_da_fila]),
    ]

    for filename, description in filenames:
        print(f"\n{description}:")
        data = read_file(filename)

        for sort_name, sort_func in sort_algorithms:
            sort_time = measure_execution_time(sort_func, data.copy())
            print(f"Tempo {sort_name}: {sort_time:.5f} segundos")

        sorted_data = sorted(data)

        for search_name, search_func in search_algorithms:
            search_time = measure_execution_time(search_func, sorted_data, sorted_data[-1])
            print(f"Tempo {search_name}: {search_time:.5f} segundos")

        for data_structure_name, operations in data_structures:
            print(f"\n{data_structure_name}:")
            for operation in operations:
                if operation == remover_da_pilha or operation == remover_da_fila:
                    exec_time = measure_execution_time(operation, data.copy())
                else:
                    exec_time = measure_execution_time(operation, data.copy(), data[-1])
                print(f"Tempo de execução {operation.__name__}: {exec_time:.5f} segundos")


if __name__ == "__main__":
    main()
