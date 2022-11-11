def fatorial_for():
    while True:
        print(f'\033[1;32m=-=-=-=- FATORIAL USANDO LOOP FOR -=-=-=-=\033[0;0m')
        n = input('Digite um número para ver seu fatorial: ')
        try:
            n = int(n)
            break
        except:
            print('\033[1;31mVocê não digitou um número!\033[0;0m')

    print(f'>>>> O fatorial de {n} é ', end='')

    contador = 1
    for cont in range(1, n+1):
        contador *= cont
    print(contador)

if __name__ == '__main__':
    fatorial_for()
