def nome(name):
    print(f'Olá, {name}!')

nome = input('Qual seu nome? ').upper()

idade = int(input('Quantos anos você tem? '))
if idade <20:
    print('Que novinho(a)')
elif idade >= 21 and idade <= 40:
    print('Como anda a vida adulta? :)')
elif idade >41:
    print('Já se aposentou? hihihi')
