from random import randint


print('ZOMBIE DICE!')
print('Seja bem-vindo ao jogo Zombie Dice!')

numJogadores = 0
while (numJogadores < 2 ):
    numJogadores = int(input('Informe a quantidade de jogadores: '))

    if (numJogadores < 2):
        print('AVISO: Você precisa de pelo menos 2 jogadores!\n')

listaJogadores = []
for i in range(numJogadores):
    nome = input('Informe o nome do jogador ' + str(i + 1) + ': ')

    listaJogadores.append(nome)


print(listaJogadores)


dadoVerde = "CPCTPC"
dadoAmarelo = "TPCTPC"
dadoVermelho = "TPTCPT"

listaDados = [dadoVerde,dadoVerde,dadoVerde,dadoVerde,dadoVerde,dadoVerde,
    dadoAmarelo,dadoAmarelo,dadoAmarelo,dadoAmarelo,
    dadoVermelho,dadoVermelho,dadoVermelho]

print('INICIANDO O JOGO...')

jogadorAtual = 0
dadosSorteados = []
tiros = 0
cerebros = 0
passos = 0

while True: 
    print('É a vez de',listaJogadores[jogadorAtual] + '...')
    break
i = 0
while (i < 2): 
    numSorteado = randint(0, 12)
    dadoSorteado = listaDados[numSorteado]