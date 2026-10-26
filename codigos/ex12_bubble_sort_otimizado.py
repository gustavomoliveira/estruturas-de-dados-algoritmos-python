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


def bubble_sort_otimizado(lista):
    resultado = lista.copy()
    comparacoes = 0
    trocas = 0

    for ultimo in range(len(resultado) - 1, 0, -1):
        houve_troca = False

        for posicao in range(ultimo):
            comparacoes += 1
            if resultado[posicao] > resultado[posicao + 1]:
                guardado = resultado[posicao]
                resultado[posicao] = resultado[posicao + 1]
                resultado[posicao + 1] = guardado
                trocas += 1
                houve_troca = True

        if not houve_troca:
            break

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

print('=== Exercício 12 – Bubble Sort otimizado ===')
print()
print(f'{"N":<6}{"Cenário":<16}{"Comp. (Ex.11)":<15}{"Comp. (Ex.12)":<15}{"Trocas (Ex.11)":<16}{"Trocas (Ex.12)":<16}')
print('-' * 84)

for tamanho in tamanhos:
    for nome, lista in gerar_cenarios(tamanho).items():
        saida_a, comparacoes_a, trocas_a = bubble_sort_contado(lista)
        saida_b, comparacoes_b, trocas_b = bubble_sort_otimizado(lista)
        if saida_a != saida_b:
            print(f'ERRO: resultados diferentes para N={tamanho}, {nome}')
        print(f'{tamanho:<6}{nome:<16}{comparacoes_a:<15}{comparacoes_b:<15}{trocas_a:<16}{trocas_b:<16}')