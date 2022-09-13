def decimal():
    while True:
        print(f'\033[1;34m =-=-=-=- GERADOR DE DECIMAIS A PARTIR DE BINÁRIOS -=-=-=-= \033[0;0m')
        n = input('Digite um número binário para ver seu correspondente decimal: ')
        try:
            n = int(n, 2)
            break
        except:
            print('\033[1;31mVocê não digitou um número inteiro ou binário!\033[0;0m')

    print(f"O número {n} em decimal é igual a: ")
    tamanho = len(str(n))
    decimal = i = 0
    while n >= 1:
        resto = n%10
        decimal = decimal + (resto*(2**i))
        tamanho -= 1
        i += 1
        n //= 10
    print(decimal)
    

if __name__ == '__main__':
    decimal()
