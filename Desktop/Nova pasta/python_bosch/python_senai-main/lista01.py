#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final mostre qual foi o maior e menor valor digitado e suas respectivas posições
valores = []
maior = menor = 0


for v in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {v+1}: ')))     #adicionando o valor digitado na lista
    if v == 0:                                                                #se for o primeiro numero a ser digitado, ele será o maior e o menor
        maior = menor = valores[v]
    else:                                                                     #comparando os valores e definindo o maior e o menor
        if valores[v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]

print(f'Você digitou os valores {valores}')

print(f'>>> O maior valor digitado foi {maior} na(s) posição(es): ', end='')
for i, v in enumerate(valores):                                               #encontrando a posição que os maiores valores foram digitados
    if v == maior:
        print(f'{i+1}... ', end='')


print(f'\n>>> O menor valor digitado foi {menor} na(s) posição(es): ', end='')
for i, v in enumerate(valores):                                               #encontrando a posição que os menores valores foram digitados
    if v == menor:
        print(f'{i+1}... ', end='')
