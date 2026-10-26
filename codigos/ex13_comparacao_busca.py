import random


def linear_search_count(arr, target):
    comparacoes = 0

    for i in range(len(arr)):
        comparacoes += 1
        if arr[i] == target:
            return i, comparacoes

    return -1, comparacoes


def binary_search_count(sorted_arr, target):
    esquerda = 0
    direita = len(sorted_arr) - 1
    comparacoes = 0

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        comparacoes += 1

        if sorted_arr[meio] == target:
            return meio, comparacoes

        if target < sorted_arr[meio]:
            direita = meio - 1
        else:
            esquerda = meio + 1

    return -1, comparacoes


def bubble_sort_count(arr):
    resultado = arr.copy()
    comparacoes = 0

    for ultimo in range(len(resultado) - 1, 0, -1):
        for p in range(ultimo):
            comparacoes += 1
            if resultado[p] > resultado[p + 1]:
                guardado = resultado[p]
                resultado[p] = resultado[p + 1]
                resultado[p + 1] = guardado

    return resultado, comparacoes


def esta_ordenada(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True


TAMANHO = 31
lista_ordenada = list(range(1, TAMANHO + 1))
lista_inversa = list(range(TAMANHO, 0, -1))
lista_aleatoria = lista_ordenada.copy()
random.seed(42)
random.shuffle(lista_aleatoria)

listas = {
    'lista_ordenada': lista_ordenada,
    'lista_inversa': lista_inversa,
    'lista_aleatoria': lista_aleatoria,
}

print('=== Exercício 13 – Comparação de estratégias de busca ===')
print()
print(f'{"Lista":<17}{"Alvo":<10}{"Valor":<7}{"Linear":<8}{"Binária":<9}{"Bubble":<8}{"Bubble+Binária":<15}')
print('-' * 74)

for nome, lista in listas.items():
    alvos = {
        'primeiro': lista[0],
        'meio': lista[TAMANHO // 2],
        'ausente': -1,
    }

    precisou_ordenar = not esta_ordenada(lista)

    if precisou_ordenar:
        lista_para_busca_binaria, comparacoes_bubble = bubble_sort_count(lista)
    else:
        lista_para_busca_binaria = lista
        comparacoes_bubble = 0

    for nome_alvo, alvo in alvos.items():
        _, comparacoes_linear = linear_search_count(lista, alvo)
        _, comparacoes_binaria = binary_search_count(lista_para_busca_binaria, alvo)

        if precisou_ordenar:
            bubble = comparacoes_bubble
            total = comparacoes_bubble + comparacoes_binaria
        else:
            bubble = '-'
            total = '-'

        print(f'{nome:<17}{nome_alvo:<10}{alvo:<7}{comparacoes_linear:<8}{comparacoes_binaria:<9}{bubble:<8}{total:<15}')