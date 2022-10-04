import inquirer
import random
import forca_img
import sys

palavra_secreta = ''
anderlines_palavra_secreta = []
palavra_sorteada = False
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
                jogo_forca()

            elif respostas['escolha'] == 'Adicionar/Remover palavra':
                add_remove()

            elif respostas['escolha'] == 'Visualizar palavras e dicas':
                view_tips_words()

            elif respostas['escolha'] == 'Sair':
                sair()


#TODO Verificar se a letra informada existe na palavra
#TODO Encontrar a posição da letra na palavra
#TODO Substituir o underline pela letra na posição
#BINARYSEARCH 

def sortear_palavra():
    palavras = open(r'./forca/palavras.txt', 'r', encoding='utf-8')
    cadastros = palavras.readlines()
    lista_palavras = []

    for word in cadastros:
        separando = word[:-1]
        lista_palavras.append(separando)

    indice_secret_word = random.randint(0, len(lista_palavras))
    palavra_secreta = lista_palavras[indice_secret_word]

    anderlines_palavra_secreta = '_ '*len(palavra_secreta)
    palavras.close()
    print(forca_img.forca1()[0], end='')
    print(anderlines_palavra_secreta)
    palavra_sorteada = True
    return indice_secret_word, palavra_secreta, anderlines_palavra_secreta
    

def print_forca(anderlines_palavra_secreta, posicao_forca):
    print(forca_img.forca1()[0], end='')
    print(anderlines_palavra_secreta)

def jogo_forca():
    if not palavra_sorteada:
        indice_secret_word, palavra_secreta, anderlines_palavra_secreta = sortear_palavra()
    while True:
            opcoes_jogo = [
                inquirer.List(
                    'escolha',
                    message = 'OPÇÕES',
                    choices = ['Pedir dica', 'Chutar letra', 'Sair']
                )
            ]

            respostas = inquirer.prompt(opcoes_jogo)

            if respostas['escolha'] == 'Pedir dica':
                dica(indice_secret_word)
                print_forca(anderlines_palavra_secreta, 0)

            elif respostas['escolha'] == 'Chutar letra':
                chute(palavra_secreta)

            elif respostas['escolha'] == 'Sair':
                sair()

            
def dica(indice_secret_word):
    acessar_dicas = open(r'./forca/dicas.txt', 'r', encoding='utf-8')
    dicas = acessar_dicas.readlines()
    dica = dicas[indice_secret_word]
    print(f'DICA =', dica)
    

def chute(palavra_secreta, anderlines_palavra_secreta):
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Ç', 'Sair']
    while True:
            letra = [
                inquirer.List(
                    'escolha',
                    message = 'TENTATIVA',
                    choices = letras
                )
            ]

            respostas = inquirer.prompt(letra)
            letras.remove(respostas['escolha'])
            verificar_letra(respostas['escolha'], palavra_secreta)

def verificar_letra(letra_escolhida, palavra_secreta):
    if letra_escolhida in palavra_secreta:
        for index, letra in enumerate(palavra_secreta):
            if letra_escolhida == letra:
                print(index, letra)
  

def add_remove():
    while True:
        opcoes = [
            inquirer.List(
                "escolha",
                message="Adicionar ou Remover Palavras",
                choices=[
                    "Remover",
                    "Adicionar",
                    "Sair",
                ],
            )
        ]
        respostas = inquirer.prompt(opcoes)

        if respostas["escolha"] == "Remover":
            remove()

        elif respostas["escolha"] == "Adicionar":
            add()

        elif respostas["escolha"] == "Sair":
            sair()
            

def add():
    palavra = input('Digite a palavra que quer adicionar: ').upper().strip()
    dica = input(f'Digite a dica para {palavra}: ').upper().strip()
    confirmar = input(f'PALAVRA = {palavra}\nDICA = {dica}\nAs informações estão corretas? ').upper().strip()
    if confirmar == 'S':
        print("\33[32mPalavra adicionada com sucesso\33[m")
        palavras = open(r'./forca/palavras.txt', 'a', encoding='utf-8')
        palavras.write(f'{palavra}\n')
        palavras.close()
        dicas = open(r'./forca/dicas.txt', 'a', encoding='utf-8')
        dicas.write(f'{dica}\n')
        dicas.close()
        return menu()
    else:
        return add_remove()


def remove():
    print('Qual palavra quer remover? ')
    abrir_palavra = open(r'./forca/palavras.txt', 'r', encoding='utf-8')
    abrir_dicas = open(r'./forca/dicas.txt', 'r', encoding='utf-8')

    print_words = abrir_palavra.readlines()
    print_tips = abrir_dicas.readlines()

    lista_palavras = []
    lista_dicas = []

    for word in print_words:
        if word.__contains__('\n'):
            lista_palavras.append(word[:-1])
        else:
            lista_palavras.append(word)

    for tip in print_tips:
        if tip.__contains__('\n'):
            lista_dicas.append(tip[:-1])
        else:
            lista_dicas.append(tip)

    palavras = [
        inquirer.List("escolha", message="Remover Palavra", choices=lista_palavras)
    ]

    respostas = inquirer.prompt(palavras)['escolha']
    abrir_palavra.close()
    indice_palavra = -1
    for indice, palavra in enumerate(lista_palavras):
        if palavra == respostas:
            indice_palavra = indice
    lista_palavras.remove(respostas)

    palavras_file = open(r'./forca/palavras.txt', 'w', encoding='utf-8')
    string_palavras = '\n'.join(lista_palavras)
    palavras_file.write(string_palavras)

    print()
    print(f'\033[1;32mPalavra {respostas} removida com sucesso!\033[0;0m')
    palavras_file.close()


    lista_dicas.pop(indice_palavra)
    dicas_file = open(r'./forca/dicas.txt', 'w', encoding='utf-8')
    string_dicas = '\n'.join(lista_dicas)
    dicas_file.write(string_dicas)
  

def view_tips_words():
    print('\033[1;96mPALAVRA\033[0;0m = \033[1;92mDICA\033[0;0m')
    abrir_palavra = open(r'./forca/palavras.txt', 'r', encoding='utf-8')
    abrir_dica = open(r'./forca/dicas.txt', 'r', encoding='utf-8')
    print_words = abrir_palavra.readlines()
    print_tips = abrir_dica.readlines()
    lista_palavras = []
    lista_dicas = []
   

    for word in print_words:
        lista_palavras.append(word.split('\n'))

    for tip in print_tips:
        lista_dicas.append(tip.split('\n'))

    for index in range(len(print_words)):
        print(f'\033[1;96m{print_words[index].strip()}\033[0;0m = \033[1;92m{print_tips[index].strip()}\033[0;0m')

    abrir_palavra.close()
    abrir_dica.close()


def sair():
    print('\033[1;35mAté a próxima DEV \U0001F47E\33[m')
    sys.exit()


if __name__ == '__main__':
    jogo_forca()
