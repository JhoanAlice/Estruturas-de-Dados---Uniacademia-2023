from .utils import measure_execution_time, read_file


def adicionar_a_fila(fila, elemento):
    fila.append(elemento)

def remover_da_fila(fila):
    return fila.pop(0)

def main():
    print("\nFila:")
    dados = read_file("small_data.txt")
    operacoes = [adicionar_a_fila, remover_da_fila]

    for operacao in operacoes:
        tempo_exec = measure_execution_time(operacao, dados.copy(), dados[-1])
        print(f"Tempo de execução {operacao.__name__}: {tempo_exec:.5f} segundos")

if __name__ == "__main__":
    main()
