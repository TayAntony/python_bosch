#criar um programa que le numero de 1000 a 9999 e mostre a milhar, dezena, centena e unidade

numero = int(input('Digite um número de 0 a 9999: '))
while True:
    if numero >9999: #tratamento para numeros maiores que 9999
        numero = int(input('Digite um número de 0 a 9999: '))
    else:    
        n = str(numero) #usando str para converter o numero para string e conseguir dividir
#dividindo o numero pelos seus respectivos divisores inteiros e armazenando numa variavel correspondente 
        unidade = numero// 1 % 10
        dezena = numero//10 % 10
        centena = numero//100 % 10
        milhar = numero//1000 % 10
        print(f'Analisando o número {numero}: ')
        print(f'Milhar: {milhar}')
        print(f'Centena: {centena}')
        print(f'Dezena: {dezena}')
        print(f'Unidade: {unidade}')
        break
