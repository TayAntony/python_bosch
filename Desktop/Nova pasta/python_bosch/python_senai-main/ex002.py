def calcular(valor1, valor2):
    resultado = valor1 + valor2
    print(f'O resultado da soma foi {resultado}')

def subtrair(valor1, valor2):
    resultado = valor1 - valor2
    print(f'O resultado da subtração foi: {resultado}')

def multiplicar(valor1, valor2):
    resultado = valor1 * valor2
    print(f'O resultado da multiplicação foi: {resultado}')

def divisão(valor1, valor2):
    resultado = valor1 / valor2
    print(f'O resultado da divisão foi: {resultado:.2f}')

def get_escolha_user():
    try:
        valor1 = int(input('Digite o primeiro número: '))
        valor2 = int(input('Digite o segundo número: '))
        opcao = int(input('''O que deseja fazer com os valores?
        [ 1 ] Somar
        [ 2 ] Subtrair 
        [ 3 ] Multiplicar
        [ 4 ] Dividir
        [ 5 ] Sair
        >>>>>>> Sua opção: '''))
        return valor1, valor2, opcao
    except:
        print('[ERRO] Por favor digite um valor válido!')
        return get_escolha_user()


while True:
    valor1, valor2, opcao = get_escolha_user()
        
    if opcao == 1:
        calcular(valor1, valor2)
    elif opcao == 2:
        subtrair(valor1, valor2)
    elif opcao == 3:
        multiplicar(valor1, valor2)
    elif opcao == 4:
        divisão(valor1, valor2)
    elif opcao == 5:
        print('Obrigada e volte sempre :)')
        break
    else:
        print('[ERRO] Por favor digite um valor válido!')
    
