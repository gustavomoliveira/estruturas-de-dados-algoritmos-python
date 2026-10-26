TOTAL_QUADRADOS = 64

def tabuleiro_xadrez(qtd_graos):
    quadrado = 1
    graos = 1

    while graos < qtd_graos and quadrado < TOTAL_QUADRADOS:
        quadrado += 1
        graos *= 2

    if graos >= qtd_graos:
        return quadrado

    return "A quantidade de grãos excede o limite do tabuleiro"


casos_teste = {
    'pequeno (1)': 1,
    'pequeno (2)': 2,
    'pequeno (4)': 4,
    'pequeno (8)': 8,
    'intermediário (1.000)': 1000,
    'intermediário (1.000.000)': 1000000,
    'último quadrado exato (2^63)': 2 ** 63,
    'acima do limite (2^63 + 1)': 2 ** 63 + 1,
    'muito acima do limite (2^64)': 2 ** 64,
}

print('=== Exercício 6 – Tabuleiro de xadrez ===')
print()

for nome, qtd_graos in casos_teste.items():
    resultado = tabuleiro_xadrez(qtd_graos)
    print(f'Caso: {nome}')
    print(f'  Grãos pedidos: {qtd_graos}')
    print(f'  Resultado: {resultado}')