def decisao (e):
    if e == 1:
        print(f'Continuou...')
    elif e == 0:
        print('Encerrou o programa...')
    else:
        print('Insira 1 ou 0')

def parImpar(valor):
    if valor %2==0:
        print('é par')
    else:
        print('é ímpar')

def validarNumero(numero):
    if numero.isnumeric():
        return True
    else:
        return False

numero = input('Digite um número: ')
if validarNumero(numero):
    numero = int(numero)
    parImpar(numero)

else:
    print('Você não digitou um número')

escolha = input('Digite 1 para continuar e 0 parar: ')
if validarNumero(escolha):
    escolha = int(escolha)
    decisao(escolha)