def find():
    palavra = 'tayssaantoniasse'.lower()
    posicoes = []
    for posicao, letra in enumerate(palavra):
        if letra == 's':
            posicoes.append(posicao)
    print(posicoes)

if __name__ == '__main__':
    find()