class senaibank:
    __num_registro = 0
    __registros = dict()
    def __init__(self, nome, fake_user):
        self.nome = nome
        self.__dinheiro = 800
        self.fake_user = fake_user

    def verificar_saque(self, valor_saque):
        if self.__dinheiro < valor_saque:
            return False
        return True
    
    def efetivar_saque(self):
        valor = int(input('Digite o valor que deseja sacar: R$'))
        if self.verificar_saque(valor):
            self.__dinheiro = self.__dinheiro - valor
            self.__registros[self.__num_registro] = f'\033[1;31mSaque efetuado com sucesso! Seu saldo atual é de: R${self.__dinheiro},00\033[0;0m'
            print(self.__registros[self.__num_registro])
            self.__num_registro += 1

        else:
            print(f'Você não tem esse valor para sacar. Saldo atual: {self.__dinheiro},00')

    def verificar_deposito(self, valor_deposito):
        if valor_deposito > 1000:
            return False
        return True

    def efetivar_deposito(self):
        valor = int(input('Digite o valor que deseja depositar: R$'))
        if self.verificar_deposito(valor):
            self.__dinheiro = self.__dinheiro + valor
            self.__registros[self.__num_registro] = f'\033[1;32mDepósito efetuado com sucesso! Seu saldo atual é de: R${self.__dinheiro},00\033[0;0m'
            print(self.__registros[self.__num_registro])
            self.__num_registro += 1
            
        else:
            print('O valor é muito alto, deposite um valor menor!')

    def verificar_transferencia(self, valor_transferencia):
        if self.__dinheiro < valor_transferencia:
            return False
        return True

    def efetivar_transferencia(self):
        valor = int(input('Digite o valor que deseja transferir: R$'))
        if self.verificar_transferencia(valor):
            self.__dinheiro = self.__dinheiro - valor
            self.__registros[self.__num_registro] = f'\033[1;31mTransferência para {self.fake_user} efetuada com sucesso! Seu saldo atual é de: R${self.__dinheiro},00\033[0;0m'
            print(self.__registros[self.__num_registro])
            self.__num_registro += 1

        else:
            print(f'Você não tem esse valor para transferir. Saldo atual: {self.__dinheiro},00')
    
    def extrato(self):
        print(f'Olá {self.nome}, você possui {self.__dinheiro} reais na sua conta.')
        print('Seu histórico é este: ')
        for i in self.__registros:
            print(f'REGISTRO Nº{i+1}: {self.__registros[i]}')