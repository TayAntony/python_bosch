
def laco_repeticao_for():
    r = list(range(1, 10, 3)) #se o valor inicial for maior que o valor final mostrará uma lista vazia
    #o primeiro parâmetro é o start, o segundo o end, e o terceiro o passo
    print(r)

    aprendizes = ['Tayssa', 'Raissa', 'Bia', 'Michael']
    notas = [10, 10, 9, 4]
    qntd_aprendizes = len(aprendizes)
    for posicao in aprendizes:
        print(aprendizes[posicao], notas[posicao])

if __name__ == '__main__':
    laco_repeticao_for()