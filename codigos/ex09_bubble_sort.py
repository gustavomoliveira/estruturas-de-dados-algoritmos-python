def bubble_sort(lista):
    resultado = lista.copy()

    for ultimo in range(len(resultado) - 1, 0, -1):
        for posicao in range(ultimo):
            if resultado[posicao] > resultado[posicao + 1]:
                guardado = resultado[posicao]
                resultado[posicao] = resultado[posicao + 1]
                resultado[posicao + 1] = guardado

    return resultado


entradas = {
    'desordenada': [64, 34, 25, 12, 22, 11, 90],
    'já ordenada': [1, 2, 3, 4, 5, 6],
    'ordem inversa': [9, 8, 7, 6, 5, 4],
    'com repetidos': [4, 2, 4, 1, 2],
    'negativos': [3, -1, 0, -5, 2],
    'decimais': [2.5, 1.5, 3.0, 0.5],
    'um elemento': [7],
    'lista vazia': [],
}

esperados = {
    'desordenada': [11, 12, 22, 25, 34, 64, 90],
    'já ordenada': [1, 2, 3, 4, 5, 6],
    'ordem inversa': [4, 5, 6, 7, 8, 9],
    'com repetidos': [1, 2, 2, 4, 4],
    'negativos': [-5, -1, 0, 2, 3],
    'decimais': [0.5, 1.5, 2.5, 3.0],
    'um elemento': [7],
    'lista vazia': [],
}

print('=== Exercício 9 – Bubble Sort numérico ===')
print()

for nome in entradas:
    entrada = entradas[nome]
    saida = bubble_sort(entrada)
    print(f'Caso: {nome}')
    print(f'  Entrada: {entrada}')
    print(f'  Saída:   {saida}')
    print(f'  Correta: {saida == esperados[nome]}')