CONFIGURACAO = {
    'destroyer': 3,
    'porta-avioes': 5,
    'submarino': 2,
    'torpedeiro': 3,
    'cruzador': 2,
    'couracado': 4
}

PAISES =  {
    'Brasil': {
        'cruzador': 1,
        'torpedeiro': 2,
        'destroyer': 1,
        'couracado': 1,
        'porta-avioes': 1
    }, 
    'França': {
        'cruzador': 3, 
        'porta-avioes': 1, 
        'destroyer': 1, 
        'submarino': 1, 
        'couracado': 1
    },
    'Austrália': {
        'couracado': 1,
        'cruzador': 3, 
        'submarino': 1,
        'porta-avioes': 1, 
        'torpedeiro': 1
    },
    'Rússia': {
        'cruzador': 1,
        'porta-avioes': 1,
        'couracado': 2,
        'destroyer': 1,
        'submarino': 1
    },
    'Japão': {
        'torpedeiro': 2,
        'cruzador': 1,
        'destroyer': 2,
        'couracado': 1,
        'submarino': 1
    }
}

ALFABETO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

CORES = {
    'reset': '\u001b[0m',
    'red': '\u001b[31m',
    'black': '\u001b[30m',
    'green': '\u001b[32m',
    'yellow': '\u001b[33m',
    'blue': '\u001b[34m',
    'magenta': '\u001b[35m',
    'cyan': '\u001b[36m',
    'white': '\u001b[37m'
}
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
    print('ALFABETO[:10]')
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

