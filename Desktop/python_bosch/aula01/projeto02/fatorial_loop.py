def fatorial_loop():
    print()
    while True:
        print(f'\033[1;32m=-=-=-=- FATORIAL USANDO LOOP WHILE -=-=-=-=\033[0;0m')
        n = input('Digite um número para ver seu fatorial: ')
        try: 
            n = int(n)
            break
        except:
            print('\033[1;31mVocê não digitou um número!\033[0;0m')

    f = 1
    print(f'>>>> O fatorial de {n} é ', end='')
    while n > 1:      #
        f *= n        #
        n -= 1        #
    print(f)          #

if __name__ == '__main__':
    fatorial_loop()
