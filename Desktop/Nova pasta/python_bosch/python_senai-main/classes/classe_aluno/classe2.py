class Aluno:
    def __init__(self,nome, notas) -> None:
        self.nome = nome
        self.notas = notas

    def media(self):
        soma = 0
        for i in self.notas:
            soma += i
        return soma / len(self.notas)

        # media = sum(self.notas) / len(self.notas)
        # return media

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def get_preco(self):
        return self.preco
    def set_preco(self, preco):
        if preco < 0:
            raise ValueError('O preço não pode ser negativo!')