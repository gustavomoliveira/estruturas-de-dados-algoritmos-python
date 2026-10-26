def cocktail_sort(lista):
    resultado = lista.copy()
    esquerdo = 0
    direito = len(resultado) - 1

    while esquerdo < direito:
        for posicao in range(esquerdo, direito):
            if resultado[posicao] > resultado[posicao + 1]:
                guardado = resultado[posicao]
                resultado[posicao] = resultado[posicao + 1]
                resultado[posicao + 1] = guardado
        direito -= 1

        for posicao in range(direito, esquerdo, -1):
            if resultado[posicao - 1] > resultado[posicao]:
                guardado = resultado[posicao]
                resultado[posicao] = resultado[posicao - 1]
                resultado[posicao - 1] = guardado
        esquerdo += 1

    return resultado


entradas = {
    'desordenada': [5, 3, 8, 1, 9, 2],
    'já ordenada': [1, 2, 3, 4, 5],
    'ordem inversa': [9, 7, 5, 3, 1],
    'menor no final': [2, 3, 4, 5, 1],
    'com repetidos': [4, 2, 4, 1, 2],
    'negativos': [3, -1, 0, -5, 2],
    'um elemento': [7],
    'lista vazia': [],
}

esperados = {
    'desordenada': [1, 2, 3, 5, 8, 9],
    'já ordenada': [1, 2, 3, 4, 5],
    'ordem inversa': [1, 3, 5, 7, 9],
    'menor no final': [1, 2, 3, 4, 5],
    'com repetidos': [1, 2, 2, 4, 4],
    'negativos': [-5, -1, 0, 2, 3],
    'um elemento': [7],
    'lista vazia': [],
}

print('=== Exercício 8 – Cocktail Sort ===')
print()

for nome in entradas:
    entrada = entradas[nome]
    saida = cocktail_sort(entrada)
    print(f'Caso: {nome}')
    print(f'  Entrada: {entrada}')
    print(f'  Saída:   {saida}')
    print(f'  Correta: {saida == esperados[nome]}')