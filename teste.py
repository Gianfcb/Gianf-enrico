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