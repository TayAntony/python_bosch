def quadrado_cheio():
    while True:
        print(f'\033[1;32m=-=-=-=- QUADRADO DE ASTERISCOS -=-=-=-=\033[0;0m')
        n = input('Digite um número para formar um quadrado preenchido: ')
        try:
            n = int(n)
            break
        except:
            print('\033[1;31mVocê não digitou um número!\033[0;0m')

    listas = ['*  '*n]
    for cont in range(1, n+1):
        print(''.join(listas))


def quadrado_vazio():
    while True:
        print(f'\033[1;34m=-=-=-=- QUADRADO DE ASTERISCOS -=-=-=-=\033[0;0m')
        n = input('Digite um número para formar um quadrado vazio: ')
        try:
            n = int(n)
            break
        except:
            print('\033[1;31mVocê não digitou um número!\033[0;0m')

    listas = ['*  '*n]

    for cont in range(1, n+1):
        if cont == 1 or cont == n:
            print(''.join(listas))
        else:
            print('*  ', '   '*(n-2), '*', sep='')

if __name__ == '__main__':
    quadrado_cheio()
    quadrado_vazio()
