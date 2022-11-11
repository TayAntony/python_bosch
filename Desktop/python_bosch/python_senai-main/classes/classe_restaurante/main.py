import inquirer
from classes import senaibank
import sys

nome = input('Digite seu nome, usuário: ')
conta = senaibank(nome=nome, fake_user='Viktor')

while True: 
    perguntas = [
        inquirer.List(
            'escolha',
            message = 'MENU',
            choices = ['Saque', 'Depósito', 'Transferência', 'Extrato', 'Sair do banco']
        )
    ]

    print('='*50)
    print(' -=-=-=-=-=-=-=-=- BANCO DA TAY -=-=-=-=-=-=-=-=-')
    print('='*50)

    respostas = inquirer.prompt(perguntas)

    if respostas['escolha'] == 'Saque':
        conta.efetivar_saque()

    elif respostas['escolha'] == 'Depósito':
        conta.efetivar_deposito()

    elif respostas['escolha'] == 'Transferência':
        conta.efetivar_transferencia()
    
    elif respostas['escolha'] == 'Extrato':
        conta.extrato()

    elif respostas['escolha'] == 'Sair do banco':
        print("\033[1;35mAté a próxima DEV \U0001F47E\33[m")
        sys.exit()
