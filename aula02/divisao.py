def divisao():
    divisor = int(input('Entre com o divisor: '))
    dividendo = int(input('Entre com o dividendo: '))

    resultado_float = divisor/dividendo
    print(f'O resultado de {divisor}/{dividendo} é {resultado_float}')
    print('O tipo de resultado é: ', type(resultado_float))

    resultado_inteiro = divisor//dividendo
    print(f'O resultado de {divisor}/{dividendo} é {resultado_inteiro}')
    print('O tipo de resultado é: ', type(resultado_inteiro))

    resto_divisao = divisor%dividendo
    print(f'O resto da divisão de {divisor}/{dividendo} é: {resto_divisao}')
    print('O tipo de resultado é: ', type(resto_divisao))



if __name__ == '__main__':
    divisao()
