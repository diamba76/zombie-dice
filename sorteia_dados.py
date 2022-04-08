from random import randint

dado = (1, 2, 3, 4, 5, 6)


def inicializaPote(dado):
    # Inicia a lista
    pote = []
    # Executa 5 vezes
    for i in range(5):
        pote.append(dado)

    return pote


def sorteiaDados(pote):
    # Pode dar problema, pois estamos removendo itens do pote, e ao final da iteração talvez não tenhamos mais 5 dados
    # Podemos utilizar o try/except para evitar o erro
    for i in range(5):
        posicao = randint(0, 5)
        faceSorteada = pote[i][posicao]

        print("Face sorteada: " + str(faceSorteada))

        # if faceSorteada == 4 or faceSorteada == 6:
        #    pote.pop(i)

    print(pote)


pote = inicializaPote(dado)

print(pote)

sorteiaDados(pote)
