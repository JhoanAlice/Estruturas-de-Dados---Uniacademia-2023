import time
import os
from typing import List, Callable

# Função para ler os dados de um arquivo .txt
def read_file(file_path: str) -> List[int]:
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [int(i.strip()) for i in data if i.strip().isdigit()]

# Função para medir o tempo de execução de uma função
def measure_time(func: Callable, data: List[int]) -> None:
    start_time = time.time()
    func(data)
    end_time = time.time()
    print(f'{func.__name__} took {end_time - start_time} seconds to execute')

# Função principal para executar todos os algoritmos em cada arquivo de dados
def main():
    # Assumindo que nao foi criado uma pasta separada para os arquivos.
    scripts_directory = os.path.dirname(os.path.realpath(__file__))

    # Listando todos os scripts de ordenação, exceto o "00 - Index.py"
    sorting_scripts = [f for f in os.listdir(scripts_directory) if f.endswith('.py') and f != '00 - Index.py']

    # Carregar cada módulo de ordenação dinamicamente
    sorting_algorithms = []
    for script in sorting_scripts:
        script_name = script[:-3]  # remover o '.py'
        module = __import__(script_name)
        # vamos supor que a função de ordenação tem o mesmo nome do script
        sorting_function = getattr(module, script_name.replace(' ', '_').lower())
        sorting_algorithms.append(sorting_function)

    # Vamos supor que você tenha um diretório "datasets" com seus arquivos .txt de dados no mesmo diretório deste script
    data_directory = os.path.join(scripts_directory, 'datasets')
    data_files = [f for f in os.listdir(data_directory) if f.endswith('.txt')]

    # Para cada arquivo de dados, execute cada algoritmo e meça o tempo de execução
    for data_file in data_files:
        print(f'\nRunning algorithms on {data_file}')
        data = read_file(os.path.join(data_directory, data_file))
        for sorting_algorithm in sorting_algorithms:
            print(f'\nRunning {sorting_algorithm.__name__} on {data_file}')
            measure_time(sorting_algorithm, data.copy())  # passamos uma cópia dos dados para não alterar a lista original

if __name__ == "__main__":
    main()
