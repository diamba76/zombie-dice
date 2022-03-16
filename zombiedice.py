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