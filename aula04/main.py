from random import randint
from time import sleep
import inquirer

class Jogo:
    def __init__(self):
        self.numero_sorteado = 0
        self.numero_jogador = 0
        self.numero_pc = 0
        self.valor_jogada = 2
        self.saldo_jogador = 0
    
    def inicio_jogo(self):
        print('\033[1;35m-=-=-=-=- CASSINO DA TAY -=-=-=-=-\033[0;0m')
        nome_jogador = input('Digite seu nome: ').upper().strip()
        sleep(0.5)
        print(f'Olá {nome_jogador}, seja bem-vindo(a)')
        print('\033[34mAS REGRAS SÃO AS SEGUINTES:')
        sleep(1)
        print('- Você escolhe um valor de 1 a 6')
        sleep(1)
        print('- O computador escolhe um valor de 1 a 6 (tirando o valor que você escolheu)')
        sleep(1)
        print('- Cada rodada vale R$ 2,00')
        sleep(1)
        print('- Um dado de 6 lados é jogado às cegas')
        sleep(1)
        print('- Vence quem tiver escolhido o valor que caiu no dado, e ganha R$ 4,00')
        sleep(1)
        print('- Se você vencer o computador pode pedir uma revanche valendo o dobro')
        sleep(1)
        print('- Se você aceitar a revanche e ganhar, ganha R$ 8,00, se perder não ganha nada\033[0;0m')
        print('-=-'*25)
        sleep(1)
        self.obter_saldo_user()

    def obter_saldo_user(self):
        while True:
            self.saldo_jogador = input(f'Com quanto de saldo gostaria de começar? ')
            if self.saldo_jogador.isnumeric():
                if float(self.saldo_jogador) > 2:
                    self.saldo_jogador = float(self.saldo_jogador)
                    self.saldo_jogador -= self.valor_jogada
                    print(f'\033[1;32mCerto! Seu saldo atual é de R${self.saldo_jogador}\033[0;0m')
                    sleep(1)
                    break
            print('\033[31mSeu saldo deve ser válido ou maior que R$ 2,00\033[0;0m')
            continue
        self.obter_numero_user()

    def obter_numero_user(self):
        opcoes_jogador = [
                inquirer.List(
                    'escolha',
                    message = 'OPÇÕES DO DADO',
                    choices = [ 1, 2, 3, 4, 5, 6]
                )
            ]

        self.numero_jogador = inquirer.prompt(opcoes_jogador)['escolha']
        self.obter_numero_pc()
        
    def obter_numero_pc(self):
        self.numero_pc = self.numero_jogador
        while True:
            if self.numero_pc == self.numero_jogador:
                self.numero_pc = randint(1, 6)
                continue
            print(f'O número do PC é: {self.numero_pc}')
            print(f'O seu número é: {self.numero_jogador}')
            sleep(1)
            self.sortear_numero()

    def sortear_numero(self):
        print('Jogando o dado... 🎲')
        sleep(1)
        self.numero_sorteado = randint(1, 6)
        print(f'O número sorteado foi: {self.numero_sorteado}')

        if self.numero_sorteado == self.numero_jogador:
             self.revanche()

        elif self.numero_sorteado == self.numero_pc:
            print('\033[1;31mInfelizmente você perdeu!\033[0;0m')
            self.print_saldo_atual()
            
            opcoes_jogar_novamente = [
                inquirer.List(
                    'escolha',
                message = 'JOGAR NOVAMENTE?',
                choices = ('Sim', 'Não'))]
            jogar_novamente = inquirer.prompt(opcoes_jogar_novamente)['escolha']

            if jogar_novamente == 'Sim':
                if self.saldo_jogador <= 0:
                    print('Você está pobre, volte depois')
                else:
                    self.saldo_jogador -= self.valor_jogada
                    self.print_saldo_atual()
                    self.obter_numero_user()
            else:
                print('😈 Pode ir passando o dinheiro 😈')
                self.print_saldo_atual()
        
        else:
            sleep(1)
            print('\033[33mEmpate\033[0;0m')
            self.sortear_numero()

    def print_saldo_atual(self):
        print(f'\033[32mSaldo atual: R$ {self.saldo_jogador}\033[0;0m')

    def revanche(self):
        print('\033[35mParabéns, você venceu! Aceita a revanche?\033[0;0m')
        self.saldo_jogador += self.valor_jogada*2
        self.print_saldo_atual()
        opcoes_revanche = [
            inquirer.List(
                'escolha',
            message = 'REVANCHE',
            choices = ('Sim', 'Não'))]
        revanche = inquirer.prompt(opcoes_revanche)['escolha']
        if revanche == 'Sim':
            if self.saldo_jogador <= 0:
                print('Você está pobre, volte depois')
            else:
                self.valor_jogada += 2
                self.obter_numero_user()
                if self.numero_sorteado == self.numero_jogador:
                    print('\033[34mParabéns, você venceu novamente! Aqui estão seus R$ 8,00\033[0;0m')
                    self.saldo_jogador += self.valor_jogada*2
                    self.print_saldo_atual()
                else: 
                    print('Na revanche eu sou o mestre HEHEHE 🤪')
        else:
            print(f'Então fique feliz com R$ {self.saldo_jogador}, covarde 🙄')
        

if __name__ == '__main__':
    dados = Jogo()
    dados.inicio_jogo()