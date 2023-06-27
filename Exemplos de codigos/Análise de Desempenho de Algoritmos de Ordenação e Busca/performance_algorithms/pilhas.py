from .utils import measure_execution_time, read_file


def adicionar_a_pilha(pilha, elemento):
    pilha.append(elemento)


def remover_da_pilha(pilha):
    return pilha.pop()


def main():
    print("\nPilha:")
    dados = read_file("small_data.txt")
    operações = [adicionar_a_pilha, remover_da_pilha]

    for operação in operações:
        if operação == remover_da_pilha:
            tempo_exec = measure_execution_time(operação, dados.copy())
        else:
            tempo_exec = measure_execution_time(operação, dados.copy(), dados[-1])
        print(
            f"Tempo de execução {operação.__name__}: {tempo_exec:.5f} segundos")


if __name__ == "__main__":
    main()
