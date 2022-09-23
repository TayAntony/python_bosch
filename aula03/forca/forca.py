import inquirer
import random
import forca_img

def menu():
    while True:
            perguntas = [
                inquirer.List(
                    'escolha',
                    message = 'MENU',
                    choices = ['Jogar','Adicionar/Remover palavra','Visualizar palavras e dicas', 'Sair']
                )
            ]
            print('='*31)
            print('=-=-=-=- FORCA DA TAY -=-=-=-=')
            print('='*31)
    
            respostas = inquirer.prompt(perguntas)

            if respostas['escolha'] == 'Jogar':
                parada = jogo_forca()
                if parada == 'parada':
                    break

            elif respostas['escolha'] == 'Adicionar/Remover palavra':
                parada = add_remove()
                if parada == 'parada':
                    break

            elif respostas['escolha'] == 'Visualizar palavras e dicas':
                parada = view_tips_words()
                if parada == 'parada':
                    break

            elif respostas['escolha'] == 'Sair':
                parada = sair()
                if parada == 'parada':
                    break

def jogo_forca():
    palavras = open(r'./forca/palavras.txt', 'r', encoding='utf-8')
   
    cadastros = palavras.readlines()
    cadastros_2 = []

    for word in cadastros:
        separando = word[:-1]
        cadastros_2.append(separando)

    qntd_letras_secret_word = random.randint(0, len(cadastros_2))
    palavra_secreta= cadastros_2[qntd_letras_secret_word]
    oculto = '_ '*len(palavra_secreta)
    forca_img.forca1()
    print(oculto)
    palavras.close()

    while True:
            opcoes_jogo = [
                inquirer.List(
                    'escolha',
                    message = 'OPÇÕES',
                    choices = ['Pedir dica','Chutar letra', 'Sair']
                )
            ]

            respostas = inquirer.prompt(opcoes_jogo)

            if respostas['escolha'] == 'Pedir dica':
                dica()

            elif respostas['escolha'] == 'Chutar letra':
                chute(palavra_secreta)

            elif respostas['escolha'] == 'Sair':
                sair()
                return 'parada'

def dica():
    acessar_dicas = open(r'./forca/dicas.txt', 'r', encoding='utf-8')
    dicas = acessar_dicas.readlines()
    print(dicas)
    

def chute(palavra_secreta):
    tentativa = input('>>> Tentativa: ')
    print(tentativa)
    forca_img.forca1()
    

def add_remove():
    pass

def view_tips_words():
    pass

def sair():
    print('\033[1;35mAté a próxima DEV \U0001F47E\33[m')
    return 'parada'
   

if __name__ == '__main__':
    jogo_forca()