def validarNumero(numero):
    if numero.isnumeric():
        return True
    else:
        return False

n1 = input('Digite um número: ')
if validarNumero(n1):
    n1 = int(n1)
    n2 = input('Digite outro número: ')
    if validarNumero(n2):
        n2 = int(n2)
        print(f'A soma de {n1} e {n2} é {n1+n2}')
    else:
        print('Você não digitou um número válido')
else: 
    print('Você não digitou um número válido')

