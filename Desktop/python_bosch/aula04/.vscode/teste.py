class Pessoas:
    def __init__(self, cor, sexo, cpf, nome, idade):
        self.cor = cor
        self.sexo = sexo
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
    
    def maiorDeIdade(self):
        if self.idade >= 18:
            print(f"{self.nome} é maior de idade")
        else:
            print(f"{self.nome} nao é maior")

def maior(idade, nome):
    if idade >= 18:
            print("maior de idade")
    else:
            print("nao é maior")

if __name__ == '__main__':
    pessoa1 = Pessoas("branco", "feminino", 5555, "Tay", 18)
    pessoa2 = Pessoas("branco", "masculino", 2222, "Gustavo", 19)
    pessoa1.maiorDeIdade()
    pessoa2.maiorDeIdade()

    idade1 = 18
    nome1 = "jessica"
    idade2 = 22
    nome2 = "roberto"
    maior(idade1, nome1)
    maior(idade2, nome2)