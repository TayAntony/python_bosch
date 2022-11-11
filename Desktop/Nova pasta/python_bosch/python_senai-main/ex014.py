#Crie um programa que percorra uma certa quantidade de valores (mínimo 10) e exiba para o usuário apenas os números pares
print('O números pares de 0 a 40 são: ')
for n in range(0,41):
    if n % 2 == 0:
        print(n, end=' ')
