def bubble_sort_strings(palavras):
    resultado = palavras.copy()

    for ultimo in range(len(resultado) - 1, 0, -1):
        for posicao in range(ultimo):
            if resultado[posicao] > resultado[posicao + 1]:
                guardado = resultado[posicao]
                resultado[posicao] = resultado[posicao + 1]
                resultado[posicao + 1] = guardado

    return resultado


entradas = {
    'frutas': ['manga', 'banana', 'uva', 'abacaxi', 'laranja'],
    'já ordenada': ['ana', 'bia', 'caio'],
    'ordem inversa': ['zebra', 'macaco', 'gato', 'abelha'],
    'repetidas': ['sol', 'lua', 'sol', 'mar'],
    'mesmo prefixo': ['casaco', 'casa', 'cas', 'casal'],
    'maiúsculas e minúsculas': ['banana', 'Abacaxi', 'uva', 'Manga'],
    'com acento': ['zebra', 'árvore', 'abelha'],
    'uma palavra': ['java'],
    'lista vazia': [],
}

esperados = {
    'frutas': ['abacaxi', 'banana', 'laranja', 'manga', 'uva'],
    'já ordenada': ['ana', 'bia', 'caio'],
    'ordem inversa': ['abelha', 'gato', 'macaco', 'zebra'],
    'repetidas': ['lua', 'mar', 'sol', 'sol'],
    'mesmo prefixo': ['cas', 'casa', 'casaco', 'casal'],
    'maiúsculas e minúsculas': ['Abacaxi', 'Manga', 'banana', 'uva'],
    'com acento': ['abelha', 'zebra', 'árvore'],
    'uma palavra': ['java'],
    'lista vazia': [],
}

print('=== Exercício 10 – Bubble Sort para strings ===')
print()

for nome in entradas:
    entrada = entradas[nome]
    saida = bubble_sort_strings(entrada)
    print(f'Caso: {nome}')
    print(f'  Entrada: {entrada}')
    print(f'  Saída:   {saida}')
    print(f'  Correta: {saida == esperados[nome]}')