import random

def bubble_sort_contado(lista):
    resultado = lista.copy()
    comparacoes = 0
    trocas = 0

    for ultimo in range(len(resultado) - 1, 0, -1):
        for posicao in range(ultimo):
            comparacoes += 1
            if resultado[posicao] > resultado[posicao + 1]:
                guardado = resultado[posicao]
                resultado[posicao] = resultado[posicao + 1]
                resultado[posicao + 1] = guardado
                trocas += 1

    return resultado, comparacoes, trocas


def gerar_cenarios(tamanho):
    random.seed(42)
    aleatoria = random.sample(range(tamanho * 10), tamanho)
    ordenada = list(range(tamanho))
    inversa = list(range(tamanho, 0, -1))
    return {
        'aleatória': aleatoria,
        'já ordenada': ordenada,
        'ordem inversa': inversa,
    }


tamanhos = [10, 20, 40, 80, 160]

print('=== Exercício 11 – Instrumentação do Bubble Sort ===')
print()
print(f'{"N":<6}{"Cenário":<16}{"Comparações":<14}{"Trocas":<10}{"N(N-1)/2":<10}')
print('-' * 56)

for tamanho in tamanhos:
    for nome, lista in gerar_cenarios(tamanho).items():
        ordenada, comparacoes, trocas = bubble_sort_contado(lista)
        esperado = tamanho * (tamanho - 1) // 2
        print(f'{tamanho:<6}{nome:<16}{comparacoes:<14}{trocas:<10}{esperado:<10}')