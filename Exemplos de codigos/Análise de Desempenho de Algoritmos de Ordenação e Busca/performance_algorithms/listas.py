from .utils import measure_execution_time, read_file


def adicionar_a_lista(lista, elemento):
    lista.append(elemento)

def remover_da_lista(lista, elemento):
    lista.remove(elemento)

def procurar_na_lista(lista, elemento):
    return elemento in lista

def main():
    print("\nLista:")
    dados = read_file("small_data.txt")
    operações = [adicionar_a_lista, remover_da_lista, procurar_na_lista]

    for operação in operações:
        tempo_exec = measure_execution_time(operação, dados.copy(), dados[-1])
        print(f"Tempo de execução {operação.__name__}: {tempo_exec:.5f} segundos")

if __name__ == "__main__":
    main()
