#Faça um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual valor a ser sacado (inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#Observação: considere que o caixa possui cédulas de R$ 1, R$ 10, R$ 20, R$ 50


print('='*30)
print('        BANCO DA TAY')
print('='*30)
saque = int(input('Qual o valor a ser sacado? R$'))
cem = cinq = vinte = dez = cinco = um = 0
while True:
    while saque - 100 >= 0:
        saque -= 100
        cem += 1
    while saque - 50 >= 0:
        saque -= 50
        cinq += 1
    while saque - 20 >= 0:
        saque -= 20
        vinte += 1
    while saque - 10 >= 0:
        saque -= 10
        dez += 1
    while saque - 5 >= 0:
        saque -= 5
        cinco += 1
    while saque - 1 >= 0:
        saque -= 1
        um += 1
    break

if cem != 0:
    print(f'Total de {cem} cédula(s) de R$100')
if cinq != 0:
    print(f'Total de {cinq} cédula(s) de R$50')
if vinte != 0:
    print(f'Total de {vinte} cédula(s) de R$20')
if dez != 0:
    print(f'Total de {dez} cédula(s) de R$10')
if cinco != 0:
    print(f'Total de {cinco} cédula(s) de R$5')
if um != 0:
    print(f'Total de {um} cédula(s) de R$1')

print('='*30)
print('Volte sempre!')
