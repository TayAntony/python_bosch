def primo_for():
    while True:
        print(f'\033[1;32m=-=-=-=- NÚMEROS PRIMOS USAND0 FOR -=-=-=-=\033[0;0m')
        n = input('Digite um número para ver se é primo: ')
        try:
            n = int(n)
            break
        except:
            print('\033[1;31mVocê não digitou um número!\033[0;0m')

    total = []
    for contador in range(1, n+1):
        if n%contador == 0:
            total.append(contador)

    if  len(total) > 2:
        print(f'{n} Não é primo, pois é divisível por : {total}')
    else:
        print(f'{n} é primo, pois é divisível por: {total}')

def primo_while():
    print()
    while True:
        print(f'\033[1;34m=-=-=-=- NÚMEROS PRIMOS USAND0 WHILE -=-=-=-=\033[0;0m')
        n = input('Digite um número para ver se é primo: ')
        try:
            n = int(n)
            break
        except:
            print('\033[1;31mVocê não digitou um número!\033[0;0m')

    total = []
    contador= 1
    while contador <= n:
        if n%contador == 0:
            total.append(contador)
        contador += 1

    if  len(total) > 2:
        print(f'{n} Não é primo, pois é divisível por : {total}')
    else:
        print(f'{n} é primo, pois é divisível por: {total}')


if __name__ == '__main__':
    primo_for()
    primo_while()
