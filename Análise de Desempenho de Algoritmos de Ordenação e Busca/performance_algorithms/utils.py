import os
import time

def remove_commas(filename):
    with open(filename, 'r') as file:
        content = file.read().replace(',', '')
    with open(filename, 'w') as file:
        file.write(content)

def read_file(filename):
    with open(filename, 'r') as file:
        content = [int(x.replace(',', '')) for x in file.read().split()]
    return content

def measure_execution_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return end_time - start_time

def main():
    directory = os.path.dirname(os.path.abspath(__file__))  # Diretório raiz do programa
    filenames = [filename for filename in os.listdir(directory) if filename.endswith(".txt")]

    for filename in filenames:
        print(f"\nArquivo: {filename}")
        remove_commas(filename)
        data = read_file(filename)
