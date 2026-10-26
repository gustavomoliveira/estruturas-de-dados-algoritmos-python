import random

VALORES_CARTAS = {
    "Ás": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Valete": 11,
    "Dama": 12,
    "Rei": 13,
}

NOMES_CARTAS = {}
for nome, valor in VALORES_CARTAS.items():
    NOMES_CARTAS[valor] = nome


def mostrar(cartas):
    nomes = []
    for carta in cartas:
        nomes.append(NOMES_CARTAS[carta])
    return ', '.join(nomes)


def ordenar_cartas(cartas):
    comparacoes = 0
    trocas = 0

    for i in range(len(cartas) - 1):
        menor = cartas[i]
        menor_index = i

        for j, valor_j in enumerate(cartas[i + 1:], start=i + 1):
            comparacoes += 1
            if valor_j < menor:
                menor = valor_j
                menor_index = j

        if menor_index != i:
            carta_salva = cartas[i]
            cartas[i] = cartas[menor_index]
            cartas[menor_index] = carta_salva
            trocas += 1

        print(f'  Rodada {i}: {mostrar(cartas)}')

    return comparacoes, trocas


print('=== Exercício 2 – Ordenação de cartas ===')
print()
print('--- Teste com 5 cartas ---')
cartas_teste = [13, 5, 1, 9, 3]
print(f'  Inicial: {mostrar(cartas_teste)}')
comparacoes, trocas = ordenar_cartas(cartas_teste)
print(f'  Final: {mostrar(cartas_teste)}')
print(f'  Comparações: {comparacoes}')
print(f'  Trocas: {trocas}')

print()
print('--- Teste com as 13 cartas ---')
random.seed(42)
cartas = list(VALORES_CARTAS.values())
random.shuffle(cartas)
print(f'  Inicial: {mostrar(cartas)}')
comparacoes, trocas = ordenar_cartas(cartas)
print(f'  Final: {mostrar(cartas)}')
print(f'  Comparações: {comparacoes}')
print(f'  Trocas: {trocas}')
print(f'  Correta: {cartas == list(VALORES_CARTAS.values())}')