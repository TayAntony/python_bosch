#fazer um programa que lê o numero do celular e corrija o numero caso contenha só 8 dígitos, e adicionar o 9 na frente

numero = input('Digite seu número de telefone com DDD [xx xxxxx-xxxx]: ')
ddd = numero[:2]
telefone = numero[2:]

while len(numero) < 10:
    numero = int(input('Digite mais que 9 valores: '))
    num = str(numero)
    ddd = numero[:2]
    telefone = numero[2:]
    

if len(numero) == 10:
    print(f'{ddd} 9 {telefone}')
else:
    print(f'{ddd} {telefone}')
