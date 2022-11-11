#Faça um programa que ajude o jogador da Mega Sena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo cadastrando tudo em uma lista composta

from time import sleep
import random
jogos = []
lista = []

print('*'*40)
print('{:^40}'.format('JOGUE NA MEGA-SENA'))
print('*'*40)

quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
total = 1
while total <= quantidade:
    cont = 0

    while True:
        num = random.randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break

    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

print(f'------ Sorteando {quantidade} jogos ------')

for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)

print('=-=-=-=-=- < Boa sorte > -=-=-=-=-=')
