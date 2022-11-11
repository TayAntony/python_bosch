minha_variavel = 0
nome = 'Tayssa '
minha_variavel= 10+8

print(f'O valor da variável é {minha_variavel}')
print(f'O nome é {nome + " Antoniasse"}')

entrada = int(input('Digite um número: '))
print(f'O valor é {minha_variavel + entrada}')

sobrenome = input('Digite seu sobrenome: ')
print(f'O nome e o sobrenome são: {nome + sobrenome}')

#escolha =  input('Quer continuar? [S/N]: ').upper().strip()
#if escolha == 's':
#    print('Continuou...')

def decisao (e):
    if e == 1:
        print(f'Continuou...')
    elif e == 0:
        print('Encerrou o programa...')
    else:
        print('Insira 1 ou 0')

escolha = input('Digite 1 para continuar e 2 parar: ')
if escolha.isnumeric():
    escolha = int(escolha)
    decisao(escolha)
else:
    print('Você não digitou um número')
