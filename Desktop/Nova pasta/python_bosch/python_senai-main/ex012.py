#Faça um programa que peça o ano de nascimento de 5 pessoas. Ao final, mostre quantas pessoas são maiores de idade (maior que 18)

from datetime import date

totmaior = 0
totmenor = 0
for pessoa in range(1,6):
    nasc = int(input(f'Digite o ano de nascimento da {pessoa}ª pessoa: '))
    atual = date.today().year
    idade = atual-nasc
    if idade<18:
        totmenor += 1
    elif idade>=18:
        totmaior += 1
print(f'Ao todo tivemos {totmenor} pessoa(s) menor(es) de idade e {totmaior} pessoa(s) maior(es) de idade!')
