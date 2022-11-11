#Desenvolva um programa que leia 6 números  inteiros e mostre a soma apenas daqueles que  forem pares. Se o valor digitado for ímpar,  desconsidere-o
totpar = 0
soma_par = 0
for n in range(1,7):
    numero = int(input('Digite um número inteiro: '))
    if numero % 2 == 0:
        totpar += 1
        soma_par = numero + soma_par

print('=-=-'*20)
print(f'Você digitou {totpar} numeros pares!')
print(f'A soma dos pares é: {soma_par} ')
