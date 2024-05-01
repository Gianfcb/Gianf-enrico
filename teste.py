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
def mostrar_mapa(mapa, mapa_inimigo):
    print("  A B C D E F G H I J")
    for i, linha in enumerate(mapa, start=1):
        print(f"{i:2}", end=" ")
        for j, elemento in enumerate(linha):
            if mapa_inimigo[i-1][j] == ' ':
                print(mapa_inimigo[i-1][j], end=" ")
            elif mapa_inimigo[i-1][j] == 'X':
                print('X', end=" ")
            else:
                print('□', end=" ")
        print()
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
        print("Opção inválida. Por favor, escolha um número válido da próxima vez.")
        return escolher_pais()

def criar_estoque_pais(pais):
    estoque = PAISES[pais]
    return estoque
def criar_estoque_computador():
    paises_list = list(PAISES.keys())
    pais_computador = random.choice(paises_list)
    estoque_computador = PAISES[pais_computador]
    return estoque_computador, pais_computador
def mostrar_mapa(mapa, mapa_inimigo):
    print("  A B C D E F G H I J")
    for i, linha in enumerate(mapa, start=1):
        print(f"{i:2}", end=" ")
        for j, elemento in enumerate(linha):
            if mapa_inimigo[i-1][j] == ' ':
                print(mapa_inimigo[i-1][j], end=" ")
            elif mapa_inimigo[i-1][j] == 'X':
                print('\u001b[31m', end=" ")
            else:
                print('□', end=" ")
        print()
def listar_posicoes_disponiveis(mapa, tamanho_barco):
    posicoes = []
    for i in range(10):
        for j in range(10):
            if j + tamanho_barco <= 10 and np.all(mapa[i, j:j+tamanho_barco] == ' '):
                posicoes.append((i, j, 'Horizontal'))
            if i + tamanho_barco <= 10 and np.all(mapa[i:i+tamanho_barco, j] == ' '):
                posicoes.append((i, j, 'Vertical'))
    return posicoes
def alocar_barcos_jogador(mapa, estoque_jogador):
    barcos_alocados = {}
    for tipo_barco, quantidade in estoque_jogador.items():
        for _ in range(quantidade):
            posicoes_disponiveis = listar_posicoes_disponiveis(mapa, CONFIGURACAO[tipo_barco])
            print(f"Você pode alocar o {tipo_barco} nas seguintes posições listadas:")
            for idx, posicao in enumerate(posicoes_disponiveis):
                print(f"{idx + 1}: Linha {ALFABETO[posicao[0]]}, Coluna {posicao[1]} ({posicao[2]})")
            opcao = int(input("Digite o número correspondente à posição desejada: "))
            if 1 <= opcao <= len(posicoes_disponiveis):
                linha, coluna, orientacao = posicoes_disponiveis[opcao - 1]
                if orientacao == 'horizontal':
                    mapa[linha, coluna:coluna+CONFIGURACAO[tipo_barco]] = tipo_barco[0].upper()
                    for j in range(coluna, coluna+CONFIGURACAO[tipo_barco]):
                        mapa[linha][j] = '■'
                else:
                    mapa[linha:linha+CONFIGURACAO[tipo_barco], coluna] = tipo_barco[0].upper()
                    for i in range(linha, linha+CONFIGURACAO[tipo_barco]):
                        mapa[i][coluna] = '■'
                barcos_alocados[tipo_barco] = barcos_alocados.get(tipo_barco, 0) + 1
            else:
                print("Opção inválida. Por favor, escolha um número válido na próxima vez.")
    return mapa, barcos_alocados
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
def marcar_acerto_mapa_inimigo(mapa, linha, coluna):
    mapa[linha][coluna] = CORES['red'] + '■' + CORES['reset']
    return mapa


