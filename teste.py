mapa = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
]

ataques_realizados = set()

def imprimir_mapa(mapa):
    print("    A  B  C  D  E  F  G  H  I  J")
    print("  +-------------------------------+")
    for i in range(len(mapa)):
        linha = ' | '.join(mapa[i])
        print(f"{i + 1} | {linha} |")
    print("  +-------------------------------+")

def realizar_ataque(mapa, linha, coluna):
    if (linha, coluna) in ataques_realizados:
        print("Você já atacou esta posição.")
        return
    ataques_realizados.add((linha, coluna))

    ataque = mapa[linha - 1][coluna]
    print(f'\nO ataque na posição {coluna}{linha} resultou em: {ataque}')

linha = int(input('Qual número da linha deseja atacar?: '))
coluna = input('Qual letra da coluna deseja atacar?: ').upper()

coluna_index = ord(coluna) - ord('A')

if linha >= 1 and linha <= 10 and coluna_index >= 0 and coluna_index <= 9:
    realizar_ataque(mapa, linha, coluna_index)
else:
    print('\nCoordenadas inválidas. Certifique-se de que a linha está entre 1 e 10, e a coluna está entre A e J.')

imprimir_mapa(mapa)
