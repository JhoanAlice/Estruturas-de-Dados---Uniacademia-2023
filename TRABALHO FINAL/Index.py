import time
import os
from typing import List, Callable

# Função para ler os dados de um arquivo .txt
def read_file(file_path: str) -> List[int]:
    with open(file_path, 'r') as file:
        lines = file.readlines()
    # Converter cada linha em um int e retornar a lista
    return [int(line.strip()) for line in lines if line.strip().isdigit()]

def main():
    algorithms_folder = 'algorithms'
    datasets_folder = 'datasets'

    algorithms = os.listdir(algorithms_folder)
    datasets = os.listdir(datasets_folder)

    for script_name in algorithms:
        module_name = script_name.replace('.py', '')
        module = __import__(f"algorithms.{module_name.replace(' ', '_').replace('-', '_').lower()}", fromlist=[''])

        function_name = script_name.replace('.py', '').replace(' - ', '_').replace(' ', '_').lower()

        if function_name.endswith('_tad'):
            function_name = function_name.replace('_tad', '')

        sorting_function: Callable[[List[int]], List[int]] = getattr(module, function_name)

        print(f"\nRunning {module_name}")

        for dataset in datasets:
            data = read_file(os.path.join(datasets_folder, dataset))
            start_time = time.time()
            result = sorting_function(data)
            end_time = time.time()
            print(f"Dataset {dataset} sorted in {end_time - start_time} seconds.")

if __name__ == "__main__":
    main()
