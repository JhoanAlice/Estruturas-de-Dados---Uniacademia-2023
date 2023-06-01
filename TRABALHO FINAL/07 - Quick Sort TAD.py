from typing import List

class Element:
    def __init__(self, value):
        self.value = value

def quick_sort(arr: List[Element]) -> List[Element]:
    """
    Esta função implementa o algoritmo Quick Sort que trabalha com tipos abstratos de dados (TADs).
    Recebe uma lista de Elementos e retorna a lista ordenada.
    """

    # Se a lista tem no máximo um elemento, ela já está ordenada
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2].value
    left = [x for x in arr if x.value < pivot]
    middle = [x for x in arr if x.value == pivot]
    right = [x for x in arr if x.value > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Neste exemplo, estamos assumindo que os elementos da lista são objetos da classe Element, que tem um atributo value. O algoritmo Quick Sort então ordena esses objetos com base no valor desse atributo.

# Você pode expandir a classe Element para incluir outros atributos conforme necessário. Por exemplo, em uma aplicação real, você poderia ter uma classe Student com atributos name e grade, e você poderia querer ordenar uma lista de estudantes com base nas notas. Nesse caso, você substituiria value por grade no algoritmo Quick Sort.