import sys

jogadas = 0
coluna1 = []
coluna2 = []
coluna3 = []
hasteInicial = []
verifica = True

def verificacao(dQual, pQual, jogadas):
    if len(dQual) == 0:
        print("MOVIMENTO INVÁLIDO")
        jogadas = jogadas
    elif len(dQual) != 0:
        if len(pQual) == 0:
            pQual.append(dQual[-1])
            del(dQual[-1])
            jogadas = jogadas + 1
            print("Ja foram %s jogada(s)" % jogadas)
        elif len(pQual) != 0:
            if pQual[-1] < dQual[-1]:
                print("MOVIMENTO INVÁLIDO!")
            else:
                pQual.append(dQual[-1])
                del(dQual[-1])
                jogadas = jogadas + 1
                print("Ja foram %s jogada(s)" % jogadas)
        
def ganhador():
    global verifica, coluna1, coluna2, coluna3, nPecas, jogadas, hasteInicial
    if coluna3 == hasteInicial:
        print('Parabéns você ganhou')
        verifica = input("Desejas jogar novamente? (Y/N): ").upper()
        if verifica == 'Y':
            coluna1 = []
            coluna2 = []
            coluna3 = []
            hasteInicial = []
            jogadas = 0
            nPecas = int(input("Número de peças: "))
            print('Seu número mínimo de jogadas é',2**nPecas-1)
            for i in range(nPecas, 0, -1):
                coluna1.append(i)
                hasteInicial.append(i)
        
            print()
            print("coluna 1:", coluna1)
            print("coluna 2:", coluna2)
            print("coluna 3:", coluna3)
            print()
            verifica = True
        elif verifica == 'N':
            print('Obrigado por jogar!!!')
            verifica = False
            sys.exit()
        
def torre(dQual, pQual, coluna1, coluna2, coluna3):
    verificacao(dQual, pQual, jogadas)
    print()
    print("coluna 1:", coluna1)
    print("coluna 2:", coluna2)
    print("coluna 3:", coluna3)
    print()
    ganhador()

while verifica == True:
    nPecas = int(input("Número de peças: "))
    print('Seu número mínimo de jogadas é',2**nPecas-1)
    for i in range(nPecas, 0, -1):
        coluna1.append(i)
        hasteInicial.append(i)
        
    print()
    print("coluna 1:", coluna1)
    print("coluna 2:", coluna2)
    print("coluna 3:", coluna3)
    print()

    while coluna3 != range(nPecas, 0, -1):
        dQual = int(input("De qual coluna você deseja mover: "))
        while dQual != 1 and dQual != 2 and dQual != 3:
            dQual = int(input("DADO INVÁLIDO! De qual coluna você deseja mover: "))
        else:
            if dQual == 1:
                dQual = coluna1
            elif dQual == 2:
                dQual = coluna2
            elif dQual == 3:
                dQual = coluna3    
        pQual = int(input("Para qual coluna você deseja mover: "))
        while pQual != 1 and pQual != 2 and pQual != 3:
            pQual = int(input("DADO INVÁLIDO! De qual coluna você deseja mover: "))
        else:
            if pQual == 1:
                pQual = coluna1
            elif pQual == 2:
                pQual = coluna2
            elif pQual == 3:
                pQual = coluna3
        
        torre(dQual, pQual, coluna1, coluna2, coluna3)
