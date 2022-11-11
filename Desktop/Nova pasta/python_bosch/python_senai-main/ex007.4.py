from time import sleep

maior = 0
menor = 0

n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
n3 = int(input('Digite o 3° número: '))
   
print(f'Analisando os números...')
sleep(1.5)

#descobrindo o maior
if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n3 and n2 > n1:
    maior = n2
else:
    maior = n3
print(f'O {maior} é o maior')


#descobrindo o menor
if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n3 and n2 < n1:
    menor = n2
else:
    menor = n3
print(f'O {menor} é o menor')
