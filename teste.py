from random import randrange
import random
import numpy as np

CONFIGURACAO = {
    'destroyer': 3,
    'porta-avioes': 5,
    'submarino': 2,
    'torpedeiro': 3,
    'cruzador': 2,
    'couracado': 4
}

PAISES = {
    'Brasil': {'cruzador': 1, 'torpedeiro': 2, 'destroyer': 1, 'couracado': 1, 'porta-avioes': 1}, 
    'França': {'cruzador': 3, 'porta-avioes': 1, 'destroyer': 1, 'submarino': 1, 'couracado': 1},
    'Austrália': {'couracado': 1, 'cruzador': 3, 'submarino': 1, 'porta-avioes': 1, 'torpedeiro': 1},
    'Rússia': {'cruzador': 1, 'porta-avioes': 1, 'couracado': 2, 'destroyer': 1, 'submarino': 1},
    'Japão': {'torpedeiro': 2, 'cruzador': 1, 'destroyer': 2, 'couracado': 1, 'submarino': 1}
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
def cria_mapa(N):
    N=10
    mapa = []
    for _ in range(N):
        linha = []
        for _ in range(N):
            linha.append(' ')
        mapa.append(linha)
    return mapa

def escolher_pais():
    print("Escolha um país para jogar:")
    for idx, pais in enumerate(PAISES.keys()):
        print(f"{idx + 1}: {pais}")
    opcao = input("Digite o número correspondente ao país que você deseja: ")
    opcao = int(opcao)
    paises_list = list(PAISES.keys())
    if 1 <= opcao <= len(paises_list):
        return paises_list[opcao - 1]
    else:
        print("Opção inválida. Por favor, escolha um país válido da próxima vez.")
        return escolher_pais()
    
def criar_estoque_pais(pais):
    estoque = PAISES[pais]
    return estoque
    
print("Bem-vindo à Batalha Naval!")

pais_jogador = escolher_pais()
estoque_jogador = criar_estoque_pais(pais_jogador)

print(f"Você escolheu jogar pelo {pais_jogador}. Seu estoque de barcos:")
print(estoque_jogador)

def criar_estoque_bot():
    paises_list = list(PAISES.keys())
    pais_bot = random.choice(paises_list)
    estoque_bot = PAISES[pais_bot]
    print(f"Você está jogando contra {pais_bot}. Prepare-se para a batalha!")
    print(f"O mapa do seu adversário ({pais_bot}):")
    return estoque_bot, pais_bot 
def mostrar_mapa(mapa, mapa_bot):
    print("  A B C D E F G H I J")
    for i, linha in enumerate(mapa, start=1):
        print(f"{i:2}", end=" ")
        for j, elemento in enumerate(linha):
            if mapa_bot[i-1][j] == ' ':
                print(mapa_bot[i-1][j], end=" ")
            elif mapa_bot[i-1][j] == 'X':
                print('\u001b[31m', end=" ")
            else:
                print('□', end=" ")
def listar_posicoes_disponiveis(mapa, tamanho_barco):
    posicoes = []
    for i in range(10):
        for j in range(10):
            if j + tamanho_barco <= 10 and np.all(mapa[i, j:j+tamanho_barco] == ' '):
                posicoes.append((i, j, 'Horizontal'))
            if i + tamanho_barco <= 10 and np.all(mapa[i:i+tamanho_barco, j] == ' '):
                posicoes.append((i, j, 'Vertical'))
    return posicoes
def barcos_jogador():
    barcos_jogador = {}
    for tipo_barco, qntd in CONFIGURACAO.items():
        barcos_jogador[tipo_barco] = qntd
    return barcos_jogador
def sorteio_de_ataque():
    return random.choice(["Jogador", "Computador"])
def mapa_bot():
    mapa_bot = np.full((10, 10), ' ')
    return mapa_bot
def ataque_jogador(mapa_bot):
    while True:
        try:
            linha = int(input("Escolha a linha para atacar de 1 a 10: ")) - 1
            coluna = int(input("Escolha a coluna para atacar de 1 a 10: ")) - 1

            if linha < 0 or linha > 9 or coluna < 0 or coluna > 9:
                print("Posição inválida. Escolha uma linha e coluna dentro do intervalo de 1 a 10.")
                continue

            if mapa_bot[linha][coluna] != ' ':
                print("Você já atacou essa posição. Escolha outra.")
                continue

            return linha, coluna
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
def foi_derrotado(linha,coluna):
        for i in linha:
            for coluna in i:
                if coluna=='N':
                    return False
        if True:
            print('Você venceu, humberto estará orgulhoso!')
        print('Você perdeu, Humberto ficará triste :( , na próxima você consegue!')
def marcar_acerto_mapa_bot(mapa, linha, coluna):
    mapa[linha][coluna] = CORES['red'] + '■' + CORES['reset']
    return mapa

