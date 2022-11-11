def fatorial(n):
   
    if n == 0:   
        print("O fatorial de 0 é 1")
    elif n < 0:   
        print("Número inválido. Escolha um valor positivo")
    elif n > 0 and n != 1:
        return n * fatorial(n - 1)
    else:
       return 1

def main():
    print()
    while True:
        print(f'\033[1;34m=-=-=-=- FATORIAL USANDO RECURSÃO -=-=-=-=\033[0;0m')
        num = input('Digite um número para ver seu fatorial: ')
        try:
            num = int(num)
            break
        except:
            print('\033[1;31mDigite um número válido!\033[0;0m')

    if num != 0 and num > 0:
        print(f'>>>> O fatorial de {num} é', fatorial(num))
        input('')
    else:
        fatorial(num)

if __name__ == '__main__':
    main()
