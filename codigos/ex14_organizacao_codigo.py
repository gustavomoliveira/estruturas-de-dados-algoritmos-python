def f(a, t):
    c = 0
    i = 0
    j = len(a) - 1
    r = -1
    while i <= j:
        m = (i + j) // 2
        c = c + 1
        if a[m] == t:
            r = m
            break
        c = c + 1
        if t < a[m]:
            j = m - 1
        else:
            i = m + 1
    return r, c


def h(arr):
    b = arr[:]
    n = len(b)
    k = 0
    for last in range(n - 1, 0, -1):
        for p in range(last):
            k += 1
            if b[p] > b[p + 1]:
                tmp = b[p]
                b[p] = b[p + 1]
                b[p + 1] = tmp
    return b, k


def busca_binaria_contada(lista_ordenada, alvo):
    comparacoes = 0
    esquerda = 0
    direita = len(lista_ordenada) - 1
    indice_encontrado = -1

    # Reduz a região de busca pela metade a cada iteração: O(log N)
    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        # Primeira comparação da iteração: igualdade com o elemento do meio
        comparacoes = comparacoes + 1
        if lista_ordenada[meio] == alvo:
            indice_encontrado = meio
            break

        # Segunda comparação da iteração: define qual metade descartar
        comparacoes = comparacoes + 1
        if alvo < lista_ordenada[meio]:
            direita = meio - 1
        else:
            esquerda = meio + 1

    return indice_encontrado, comparacoes


def bubble_sort_contado(lista):
    # Trabalha em uma cópia para não alterar a lista original
    lista_ordenada = lista.copy()
    comparacoes = 0

    # Cada passada fixa o maior elemento da região no seu lugar: O(N²)
    for ultimo in range(len(lista_ordenada) - 1, 0, -1):
        for posicao in range(ultimo):
            comparacoes += 1

            # Troca os vizinhos se estiverem fora de ordem
            if lista_ordenada[posicao] > lista_ordenada[posicao + 1]:
                guardado = lista_ordenada[posicao]
                lista_ordenada[posicao] = lista_ordenada[posicao + 1]
                lista_ordenada[posicao + 1] = guardado

    return lista_ordenada, comparacoes


lista_busca = [2, 4, 6, 8, 10, 12, 13]
lista_grande = list(range(1, 32))

listas_busca = {
    'alvo no meio': lista_busca,
    'primeiro elemento': lista_busca,
    'último elemento': lista_busca,
    'alvo ausente': lista_busca,
    'alvo maior que todos': lista_busca,
    'lista de 31 elementos': lista_grande,
    'lista vazia': [],
}

alvos_busca = {
    'alvo no meio': 8,
    'primeiro elemento': 2,
    'último elemento': 13,
    'alvo ausente': 5,
    'alvo maior que todos': 100,
    'lista de 31 elementos': 20,
    'lista vazia': 3,
}

casos_ordenacao = {
    'desordenada': [5, 3, 8, 1],
    'já ordenada': [1, 2, 3, 4, 5],
    'ordem inversa': [9, 7, 5, 3, 1],
    'com repetidos': [4, 2, 4, 1, 2],
    'um elemento': [7],
    'lista vazia': [],
}

print('=== Exercício 14 – Refatoração ===')
print()
print('--- Busca binária: original x refatorada ---')
print(f'{"Caso":<24}{"Original":<12}{"Refatorada":<12}Iguais')
print('-' * 56)
for nome in listas_busca:
    resultado_original = f(listas_busca[nome], alvos_busca[nome])
    resultado_novo = busca_binaria_contada(listas_busca[nome], alvos_busca[nome])
    print(f'{nome:<24}{str(resultado_original):<12}{str(resultado_novo):<12}{resultado_original == resultado_novo}')

print()
print('--- Bubble Sort: original x refatorado ---')
print(f'{"Caso":<24}{"Comp. original":<16}{"Comp. refatorado":<18}Iguais')
print('-' * 64)
for nome, lista in casos_ordenacao.items():
    resultado_original = h(lista)
    resultado_novo = bubble_sort_contado(lista)
    print(f'{nome:<24}{resultado_original[1]:<16}{resultado_novo[1]:<18}{resultado_original == resultado_novo}')