#Crie um programa que permita ao usuário digitar 5 valores numéricos e cadastre-os em uma lista já na posição correta de inserção (sem usar o sort()).No final mostre a lista ordenada na tela

lista = []
maior = menor = 0
for v in range(0,5):
    valor = int(input('Digite um valor: '))
    if v == 0 or valor > lista[-1]:       # se o primeiro valor for igual a 0 ou o valor digitado for maior que os outros valores percorrendo a lista o valor é adicionado na lista na ultima posição
        lista.append(valor)
        print('Adicionado ao final da lista...')
    else:
        posicao = 0                       #inicializa na posição 0
        while posicao < len(lista):
            if valor <= lista[posicao]:
                lista.insert(posicao, valor)
                print(f'Adicionado na posição {posicao+1} da lista...')
                break
            posicao += 1 
print('-='*30)
print(f'Você digitou {lista}')
