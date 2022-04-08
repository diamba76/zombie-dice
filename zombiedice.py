from random import randint


print('ZOMBIE DICE!')
print('Seja bem-vindo ao jogo Zombie Dice!')

numJogadores = 0
while numJogadores < 2:
    numJogadores = int(input('Informe a quantidade de jogadores: '))

    if numJogadores < 2:
        print('AVISO: Você precisa de pelo menos 2 jogadores!\n')

listaJogadores = []
for i in range(numJogadores):
    nome = input('Informe o nome do jogador ' + str(i + 1) + ': ')

    listaJogadores.append(nome)


dadoVerde = "CPCTPC"
dadoAmarelo = "TPCTPC"
dadoVermelho = "TPTCPT"

listaDados = [
                dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde,
                dadoAmarelo, dadoAmarelo, dadoAmarelo, dadoAmarelo,
                dadoVermelho, dadoVermelho, dadoVermelho
]

print('INICIANDO O JOGO...')

jogadorAtual = 0
dadosSorteados = []
tiros = 0
cerebros = 0
passos = 0

i = 0
while i < 3:
    print('É a vez de', listaJogadores[jogadorAtual] + '...')
    i = i + 1
    numSorteado = randint(0, 12)
    dadoSorteado = listaDados[numSorteado]

    if numSorteado <= 5:
        corDado = 'VERDE'
    elif(numSorteado > 5) and (numSorteado <= 9):
        corDado = 'AMARELO'
    else:
        corDado = 'VERMELHO'
    
    print('Dado sorteado: ', corDado)

    numSorteado = dadoSorteado
    
    