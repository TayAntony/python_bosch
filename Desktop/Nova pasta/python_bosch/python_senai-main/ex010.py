#criar um programa que leia um nome completo, mostre o nome com letras maiúsculas, minusculas, a quantidade de letras com e sem espaços e a quantidade de letras do primeiro nome

nome = input('Digite seu nome completo: ')
pnome = nome.split()[0]
nome_sem_espaço = nome.replace(' ', '')

print('=-'*30)
print(f'Seu nome em maiúsculas: {nome.upper()}')
print(f'Seu nome em minúsculas: {nome.lower()}')
print(f'Seu nome tem {len(nome)} letras com espaços, e {len(nome_sem_espaço)} letras sem espaços!')
print(f'Seu primeiro nome tem {len(pnome)} letras')
