def contador():
    print('CONTANDO DE 1 EM 1:')
    for contador in range (1, 11):
        print(contador, end=' ')
    print()

    print('CONTANDO DE 3 EM 3:')
    for contador in range (1, 11, 3):
        print(contador, end=' ')

if __name__ == '__main__':
    contador()