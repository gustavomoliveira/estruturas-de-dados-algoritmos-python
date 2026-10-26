import random

def busca_linear(lista, alvo):
    contador = 0
    for i in range(len(lista)):
        contador += 1
        if lista[i] == alvo:
            return i, contador
    return -1, contador


random.seed(42)
numeros_distintos = random.sample(range(50000), 10000)
alvo = numeros_distintos[0]
posicao, total_comparacoes = busca_linear(numeros_distintos, alvo)

print('=== Exercício 1 – Busca linear ===')
print()
print('--- Dados ---')
print(f'  Elementos distintos: {len(set(numeros_distintos))}')
print(f'  Primeiros 10 elementos: {numeros_distintos[:10]}')
print()
print('--- Busca ---')
print(f'  Alvo (primeiro elemento): {alvo}')
print(f'  Posição encontrada: {posicao}')
print(f'  Total de comparações: {total_comparacoes}')