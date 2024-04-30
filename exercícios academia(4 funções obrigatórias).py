def cria_mapa(N):
    mapa = []
    for _ in range(N):
        linha = []
        for _ in range(N):
            linha.append(' ')
        mapa.append(linha)
    return mapa

def posicao_suporta(mapa, blocos, linha, coluna, orientacao):
    altura = len(mapa)
    largura = len(mapa[0])
    if (linha < 0 or coluna < 0 or
            (orientacao == 'v' and linha + blocos > altura) or
            (orientacao == 'h' and coluna + blocos > largura)):
        return False

    for i in range(blocos):
        if orientacao == 'v':
            if mapa[linha + i][coluna] != ' ':
                return False
        else:
            if mapa[linha][coluna + i] != ' ':
                return False

    return True

import random

def aloca_navios(mapa, blocos):
    n = len(mapa)
    for tamanho_navio in blocos:
        navio_alocado = False
        while not navio_alocado:
            linha = random.randint(0, n-1)
            coluna = random.randint(0, n-1)
            orientacao = random.choice(['h', 'v'])
            
            if orientacao == 'h':
                if coluna + tamanho_navio <= n:
                    navio_encaixa = True
                    for j in range(coluna, coluna + tamanho_navio):
                        if mapa[linha][j] != ' ':
                            navio_encaixa = False
                            break
                    if navio_encaixa:
                        for j in range(coluna, coluna + tamanho_navio):
                            mapa[linha][j] = 'N'
                        navio_alocado = True
            else:
                if linha + tamanho_navio <= n:
                    navio_encaixa = True
                    for i in range(linha, linha + tamanho_navio):
                        if mapa[i][coluna] != ' ':
                            navio_encaixa = False
                            break
                    if navio_encaixa:
                        for i in range(linha, linha + tamanho_navio):
                            mapa[i][coluna] = 'N'
                        navio_alocado = True
    return mapa

def foi_derrotado(l):
    for i in l:
        for j in i:
            if j=='N':
                return False
    return True