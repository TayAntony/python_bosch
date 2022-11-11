#crie um programa que peça o nome completo e mostre de trás para frente em letras maiúsculas

nome = input('Digite seu nome completo: ').upper()
print(f'Seu nome ao contrário é: {nome[::-1]}')
