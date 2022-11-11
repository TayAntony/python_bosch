def pascal():
    while True:
        print(f'\033[1;34m=-=-=-=-=-=-=- GERADOR DE PASCAL -=-=-=-=-=-=-=-= \033[0;0m')
        n = input('Digite um número para ver seu triângulo de pascal: ')
        try:
            n = int(n)
            if n < 0:
                 print('\033[1;31mVocê não digitou um número positivo\033[0;0m')
                 return pascal()
            break
        except:
            print('\033[1;31mVocê não digitou um número!\033[0;0m')

    lista_atual = []
    lista_aux = [1]

    for base_atual in range(0, n):
        for posicao in range(0, base_atual+1):
            if posicao == 0 or posicao == base_atual:
                lista_atual.append(1)
            else:
                lista_atual.append(lista_aux[posicao] + lista_aux[posicao-1])
        lista_aux = lista_atual[:]
       
        print(*lista_atual)
        lista_atual.clear()

if __name__ == '__main__':
    pascal()