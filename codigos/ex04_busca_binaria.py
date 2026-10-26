def busca_binaria(lista, alvo):
    esquerda = 0
    direita = len(lista) - 1
    comparacoes = 0

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        comparacoes += 1

        if lista[meio] == alvo:
            return meio, comparacoes

        if alvo < lista[meio]:
            direita = meio - 1
        else:
            esquerda = meio + 1

    return -1, comparacoes


lista_ordenada = [2, 4, 6, 8, 10, 12, 13]
alvos = [8, 2, 13, 5, 100]

print('=== Exercício 4 – Busca binária ===')
print()
print(f'{"Alvo":<8}{"Índice":<10}{"Comparações":<12}')
print('-' * 30)

for alvo in alvos:
    indice, comparacoes = busca_binaria(lista_ordenada, alvo)
    print(f'{alvo:<8}{indice:<10}{comparacoes:<12}')