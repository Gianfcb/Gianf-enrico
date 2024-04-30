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
                print('X', end=" ")
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