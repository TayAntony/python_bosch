#Crie um programa que irá ler vários valores numéricos colocar em uma lista, depois disso crie 2 listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final mostre o conteúdo das 3 listas geradas

lista = []
pares = []
impares = []

while True:
    lista.append(int(input('Digite um número: ')))
    p = input('Quer continuar? [S/N]: ').upper().strip()
    if p in 'N':
        break

for i, v in enumerate(lista):
    if v%2==0:
        pares.append(v)
    else:
        impares.append(v)

print('*'*30)
print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {pares}')
print(f'A lista de ímpares é: {impares}')
print('===== FIM DO PROGRAMA =====')
