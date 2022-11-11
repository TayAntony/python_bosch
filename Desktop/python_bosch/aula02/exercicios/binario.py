def binario():
    while True:
        print(f'\033[1;34m =-=-=-=-=-=-=- GERADOR DE BINÁRIOS -=-=-=-=-=-=-= \033[0;0m')
        n = input('Digite um número para ver seu correspondente binário: ')
        try:
            n = int(n)
            if n < 0:
                print('\033[1;31mVocê não digitou um número positivo\033[0;0m')
                return binario()
            break
        except:
            print('\033[1;31mVocê não digitou um número! \033[0;0m')
    
    print(f"O número {n} em binário é igual a: ")
    binarios = ''
    while n > 0:
        if n%2==0:
            n /= 2
            binarios +='0'         
        else:                      
            n /= 2
            n = int(n)             #transformando o número decimal gerado pela divisão inteira em um número inteiro para uma nova divisão
            binarios +='1'

    binarios = binarios[::-1]      #correndo a lista binarios ao contrário para printar os números na direção certa
    print(binarios)

if __name__ == '__main__':
    binario()