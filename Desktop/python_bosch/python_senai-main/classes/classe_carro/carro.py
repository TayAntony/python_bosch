import inquirer
import sys

class Veiculo():
    def __init__(self, marca, modelo, placa, consumo, nivelCombustivel):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.consumo = consumo
        self.nivelCombustivel = nivelCombustivel 
   

class Carro(Veiculo):
    def __init__(self, categoria, airbags, litrosPortaMala, conversivel, marca, modelo, placa, consumo, nivelCombustivel):
        super().__init__(marca, modelo, placa, consumo, nivelCombustivel)
        self.categoria = categoria
        self.airbags = airbags
        self.litrosPortaMala = litrosPortaMala
        self.conversivel = conversivel

    def resumo_carro(self):
        print(f'''
\033[1;34mMarca:\033[0;0m \033[1;32m{self.marca}\033[0;0m
\033[1;34mModelo:\033[0;0m \033[1;32m{self.modelo}\033[0;0m
\033[1;34mPlaca:\033[0;0m \033[1;32m{self.placa}\033[0;0m
\033[1;34mConsumo (km/L):\033[0;0m \033[1;32m{self.consumo}\033[0;0m
\033[1;34mTanque:\033[0;0m \033[1;32m{self.nivelCombustivel}\033[0;0m
\033[1;34mCategoria:\033[0;0m \033[1;32m{self.categoria}\033[0;0m
\033[1;34mQuantidade Airbags:\033[0;0m \033[1;32m{self.airbags}\033[0;0m
\033[1;34mLitros do porta-mala:\033[0;0m \033[1;32m{self.litrosPortaMala}\033[0;0m
\033[1;34mConversível?\033[0;0m \033[1;32m{self.conversivel}\033[0;0m
''')


class Ia:
    def __init__(self, running, distancia, velocidade):
        self.running = running
        self.distancia = distancia
        self.velocidade = velocidade


class Menu():
    def __init__(self, carro, ia):
        self.carro = carro
        self.ia = ia
        self.carteira = 500

    def start(self):
        self.menu()
    
    def menu(self):
        opcoes = [
        inquirer.List(
            'escolha',
            message = 'MENU DE OPÇÕES',
            choices = ('Acelerar', 'Desacelerar', 'Manutenir', 'Finanças', 'Sair')
            )
        ]

        respostas = inquirer.prompt(opcoes)

        if respostas['escolha'] == 'Acelerar':
            self.acelerar()

        elif respostas['escolha'] == 'Desacelerar':
            self.desacelerar()
        
        elif respostas['escolha'] == 'Manutenir':
            self.manutenir()

        elif respostas['escolha'] == 'Finanças':
            self.financas()

        elif respostas['escolha'] == 'Sair':
            self.sair()
            
            
    def acelerar(self):
        self.ia.velocidade += 10
        print('Sua velocidade foi aumentada em 10km/h')
        print(f'Velocidade atual: {self.ia.velocidade}')
        if self.ia.velocidade > 80:
                print('Você recebeu uma multa de R$50,00 por excesso de velocidade (Máximo 80km/h)!')
                self.carteira -= 50
        elif self.ia.velocidade == 80:
            print('Atenção! Você está na velocidade máxima permitida na rodovia.')
        self.menu()


    def desacelerar(self):
        if self.ia.velocidade == 0:
            print('A velocidade já está em 0km/h!')
        else:
            self.ia.velocidade -= 10
            print('Sua velocidade foi reduzida em 10km/h')
            print(f'Velocidade atual: {self.ia.velocidade}')
        self.menu()


    def manutenir(self):
        print('Indo ao mecânico!')
        opcoes_mecanico = [
            'Trocar pneus - R$300,00', 
            'Trocar óleo - R$50,00', 
            'Lavagem completa - R$150,00', 
            'Calibragem - R$30,00', 'Voltar'
        ]
        
        valores = {
            'Trocar pneus - R$300,00': 300,
            'Trocar óleo - R$50,00': 50,
            'Lavagem completa - R$150,00': 150,
            'Calibragem - R$30,00': 30, 
            'Voltar': 0
        }
        
        opcoes = [
        inquirer.List(
            'escolha',
            message = 'MECÂNICO',
            choices = opcoes_mecanico
            )
        ]

        escolha = inquirer.prompt(opcoes)['escolha']

        if escolha == 'Voltar':
            return self.menu()

        valor = valores[escolha]
        if valor > self.carteira:
            print('Valor insuficiente na carteira para efetuar pagamento!')
        else:
            print('Pagamento efetuado com sucesso!')
            self.carteira -= valor
            print(f'Valor na carteira: R$ {self.carteira},00')
        
        self.menu()


    def financas(self):
        opcoes = [
        inquirer.List(
            'escolha',
            message = 'SUA CARTEIRA',
            choices = ('Saldo', 'Adicionar dinheiro', 'Sacar', 'Voltar')
            )
        ]

        escolha = inquirer.prompt(opcoes)['escolha']

        if escolha == 'Saldo':
            print(f'Valor na carteira: R$ {self.carteira},00')

        elif escolha == 'Adicionar dinheiro':
            add = int(input('Digite o valor que quer adicionar: R$'))
            self.carteira += add
            print('Valor adicionado com sucesso!')

        elif escolha == 'Sacar':
            saque = int(input('Digite o valor que quer sacar: R$'))
            self.carteira -= saque
            print('Valor sacado com sucesso!')

        self.menu()

    def sair(self):
        sys.exit()
        
