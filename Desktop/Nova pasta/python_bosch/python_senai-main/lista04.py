#Crie um programa que irá ler vários valores numéricos colocar em uma lista, depois disso mostre: Quantos números foram digitados A lista de valores ordenados de forma decrescente Se o valor 5 foi digitado e está ou não na lista

lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    p = input('Quer continuar? [S/N]: ').upper().strip()
    if p in 'N':
        break

print('*'*40)

print(f'Você digitou {len(lista)} elementos')

lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')

if 5 in lista:
        print('O valor 5 foi digitado...')
else:
    print(f'O valor 5 não foi digitado...')
