#Crie um programa que peça ao usuário um número (N) e depois a quantidade de vezes que  esse número deve ser multiplicado (Y). Exiba o resultado para cada uma das multiplicações  realizadas

numero = int(input('Digite um número: '))
quantidade = int(input('Digite quantas vezes esse número será multiplicado: '))
print('=-=-'*20)
inicio = 0
while True: 
    if quantidade <=0:
        print('Digite um número maior que 0')
        quantidade = int(input('Digite quantas vezes esse número será multiplicado: '))
    else:
        break
    
for inicio in range (1, quantidade+1):
    print(f'O RESULTADO DE {numero} x {inicio} = {numero*inicio}')
