def triangulo():
    while True:
        print(f'\033[1;34m=-=-=-=- TRIÂNGULO DE ASTERISCOS -=-=-=-=	\033[0;0m')
        n = input('Digite um número para formar a base de um triangulo: ')
        try:
            n = int(n)
            break
        except:
            print('\033[1;32mVocê não digitou um número!\033[0;0m')

    for cont in range(1, n+1):
        print('* ' * cont)
    
if __name__ == '__main__':
    triangulo()