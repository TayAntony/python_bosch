class Aluno:
    def __init__(self,nome, nota ) -> None:
        self.nota = nota
        self.nome = nome

    def media(self):
        if self.nota >= 7:
            return True
        return False

while True:
    estudante = Aluno(input('Qual seu nome? '), float(input('Digite sua nota: ')))
    if estudante.media():
        print(f'Olá {estudante.nome}! Você tem {estudante.nota} de média, e não está de recuperação')
    else:
        print(f'Olá {estudante.nome}! Você tem {estudante.nota} de média, e está de recuperação')