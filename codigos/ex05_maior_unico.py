def maior_unico(arr):
    """
    Retorna o maior número que aparece exatamente uma vez no array.
    """

    maior = None  # Guardará o maior número único encontrado

    # Percorre cada elemento do array
    for i in range(len(arr)):
        atual = arr[i]
        contador = 0  # Contará quantas vezes 'atual' aparece

        # Compara o elemento atual com todos os outros
        for j in range(len(arr)):
            if arr[j] == atual:
                contador += 1

        # Se apareceu exatamente uma vez, é um candidato
        if contador == 1:
            # Atualiza o maior único encontrado
            if (maior is None) or (atual > maior):
                maior = atual

    return maior


def maior_unico_otimizado(arr):
    contagens = {}

    for numero in arr:
        contagens[numero] = contagens.get(numero, 0) + 1

    maior = None

    for numero, quantidade in contagens.items():
        if quantidade == 1:
            if maior is None or numero > maior:
                maior = numero

    return maior


casos_teste = {
    'principal': [4, 9, 2, 9, 7, 4, 1, 7, 5],
    'maior valor repetido': [3, 8, 8, 5, 1, 5, 2],
    'todos únicos': [6, 2, 10, 4, 8],
    'todos repetidos': [3, 3, 5, 5, 5],
    'lista vazia': [],
    'um elemento': [42],
    'negativos': [-3, -1, -1, -7, -3, -5],
}

print('=== Exercício 5 – Maior número único ===')
print()
print(f'{"Caso":<22}{"Original":<10}{"Otimizada":<11}Iguais')
print('-' * 50)

for nome, arr in casos_teste.items():
    resultado_original = maior_unico(arr)
    resultado_otimizado = maior_unico_otimizado(arr)
    iguais = resultado_original == resultado_otimizado
    print(f'{nome:<22}{str(resultado_original):<10}{str(resultado_otimizado):<11}{iguais}')