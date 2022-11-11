class Aluno:
    escola = 'Senai'
    #2 tipos de atributos:
    #-> ATRIBUTOS DE CLASSE
    #-> ATRIBUTOS INSTANCIADOS
    def __init__(self, nome, ano) -> None:
        #MÉTODOS MÁGICOS -> __INIT__, __MAIN__, __NAME__
        self.nome = nome
        self.ano = ano

    def maior(self):
        if 2022 - self.ano >= 18:
            return True
        return False
    
aluno1 = Aluno('Tay', 2003)
print(aluno1.maior())

if aluno1.maior():
    print('chamar função pra aluno de maior')
else:
    print('não foi possivel, volte ano que vem')
    
print(f'A {aluno1.nome} estuda no {aluno1.escola}') #print senai
Aluno.escola = 'SESI' #atribuindo um valor na classe (print sesi)
aluno1.escola = 'SESI' #atribuindo um valor apenas no objeto, não na classe (print sesi)
print(Aluno.escola) 
print(aluno1.escola)