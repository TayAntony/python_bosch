#Crie um programa que permita ao usuário digitar vários valores numéricos e cadastre-os em uma lista. Caso o número exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

num = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in num:                                                    # verificando se o valor está na lista
        num.append(valor)
        print('Valor adicionado com sucesso... ')
    else:
        print('Valor duplicado. Escolha outro...')
    continuar = input('Quer continuar? [S/N]: ').upper().strip()
    if continuar in 'N':
        break
print('*-'*30)
num.sort()
print(f'Você digitou os valores {num}')
