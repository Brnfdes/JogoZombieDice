import random

print("---------- ZOMBIE DICE -----------")
print("Seja bem-vindo ao jogo Zombie Dice")
print("----------------------------------")

numjogadores = 0

numJogadores = 0
while numJogadores < 2:
    numJogadores = int(input('Informe a quantidade de jogadores: '))

    if numJogadores < 2:
        print('AVISO: Você precisa de pelo menos 2 jogadores!\n')

listajogadores = []

for i in range(numJogadores):
    nome = input("Qual é o nome do jogador " + str (i+1) + ": " )
    listajogadores.append(nome)
    print(listajogadores)

#definir os dados
dadoVerde = "CPCTPC"
dadoAmarelo = "TPCTPC"
dadoVermelho = "TPTCPT"

#tupla dos 13 dados disponíveis para jogar
listaDados = (dadoVerde,dadoVerde,dadoVerde,dadoVerde,dadoVerde,dadoVerde,dadoAmarelo,dadoAmarelo,dadoAmarelo,dadoAmarelo,dadoVermelho, dadoVermelho, dadoVermelho)

jogadorAtual = 0
dadosSorteados = []
cerebros = 0
tiros = 0
passos = 0
qtddados = 0

print("-------------------------------------------------------------------")
print("INICIANDO O JOGO...")
print("-------------------------------------------------------------------")

while True:
    print("TURNO DO JOGADOR", listajogadores[jogadorAtual])
    for i in range(0,3):
        numSorteado = random.randint(0, 12)
        dadoSorteado = listaDados[numSorteado]
        if dadoSorteado == "CPCTPC":
            corDado = "verde"
        elif dadoSorteado == "TPCTPC":
            corDado = "amarelo"
        else:
            corDado = "vermelho"

        print("Seu dado sorteado foi:",corDado)
        dadosSorteados.append(dadoSorteado)

    print("As faces sorteadas foram: ")
    for dadoSorteado in dadosSorteados:
        numFaceDados = random.randint(0,5)
        if dadoSorteado[numFaceDados] == "C":
            print("CÉREBRO (você comeu um cérebro)")
            cerebros = cerebros + 1
        elif dadoSorteado[numFaceDados] == "T":
            print("TIRO (você levou um tiro)")
            tiros = tiros + 1
        else:
            print("PASSOS(uma vítima escapou)")
            passos = passos + 1
    print("SCORE ATUAL: ")
    print("cérebros", cerebros)
    print("tiros", tiros)
    if cerebros >= 13:
        print("Você é o ganhador!!!")
        break
    elif tiros >= 3:
        print("Perdeu o jogo")
        del (listajogadores[jogadorAtual])
        tiros = 0
        passos = 0
        cerebros = 0
        print("Finalizando a rodada...")
        print("-------------------------------------------------------------------")
    else:
        print("-------------------------------------------------------------------")
        continuar = input("Você deseja continuar jogando os dados? digite 'sim' ou 'nao': ")
        if continuar == "nao":
            jogadorAtual = jogadorAtual + 1
            dadosSorteados = []
            tiros = 0
            passos = 0
            cerebros = 0
            print("Finalizando a rodada...")
            print("-------------------------------------------------------------------")
        else:
            print("Iniciando mais uma rodada do turno atual...")
            print("-------------------------------------------------------------------")
            dadosSorteados = []
