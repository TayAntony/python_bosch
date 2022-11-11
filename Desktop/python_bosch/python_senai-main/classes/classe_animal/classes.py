class Animal:
    def __init__(self, nome='', especie='', peso=0): #atributos NÃO PARÂMETROS
        self.nome = nome
        self.especie = especie
        self.peso = peso
        self.genero = ''
    
    def cacar(self):
        if self.especie == 'roedor':
            print(f'{self.nome} running away')
        else:
            print(f'{self.nome} on the hunt')
    
    def sexo(self):
        if self.nome.endswith('a'):
            self.genero = "F"
        else:
            self.genero = "M"

