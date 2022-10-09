
import inquirer
import random
import forca_img
import sys

PALAVRA_SECRETA = ''
ANDERLINES_PALAVRA_SECRETA = []
PALAVRA_SORTEADA = False
INDICE_SECRET_WORD = ''
TENTATIVAS = 6
LETRAS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
CHUTES = []

def menu():
    global PALAVRA_SECRETA, ANDERLINES_PALAVRA_SECRETA, PALAVRA_SORTEADA, INDICE_SECRET_WORD, TENTATIVAS, LETRAS, CHUTES
    PALAVRA_SECRETA = ''
    ANDERLINES_PALAVRA_SECRETA = []
    PALAVRA_SORTEADA = False
    INDICE_SECRET_WORD = ''
    TENTATIVAS = 6
    LETRAS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    CHUTES = []

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


#TODO ARRUMAR A REMOÇÃO DE PALAVRAS

def sortear_palavra():
    global ANDERLINES_PALAVRA_SECRETA, PALAVRA_SECRETA, INDICE_SECRET_WORD, PALAVRA_SORTEADA

    palavras = open(r'./palavras.txt', 'r', encoding='utf-8')
    cadastros = palavras.readlines()
    lista_palavras = []

    for word in cadastros:
        separando = word[:-1]
        lista_palavras.append(separando)

    INDICE_SECRET_WORD = random.randint(0, len(lista_palavras)-1)
    PALAVRA_SECRETA = lista_palavras[INDICE_SECRET_WORD]

    ANDERLINES_PALAVRA_SECRETA = list('_'*len(PALAVRA_SECRETA))
    palavras.close()
    PALAVRA_SORTEADA = True
    return INDICE_SECRET_WORD, PALAVRA_SECRETA, ANDERLINES_PALAVRA_SECRETA
    

def print_forca():
    global ANDERLINES_PALAVRA_SECRETA
    print(forca_img.forca1()[TENTATIVAS], end='')
    print(' '.join(ANDERLINES_PALAVRA_SECRETA))


def jogo_forca():
    if not PALAVRA_SORTEADA:
        INDICE_SECRET_WORD, PALAVRA_SECRETA, ANDERLINES_PALAVRA_SECRETA = sortear_palavra()

    while True:

        if ''.join(ANDERLINES_PALAVRA_SECRETA) == PALAVRA_SECRETA:
            print_forca()
            print('''
\033[32mPARABÉNS, VOCÊ ACERTOU!
            \033[0;0m''')
            menu()
        elif TENTATIVAS == 0:
            print_forca()
            print('''
\033[1;91mVOCÊ É BRONZE E PERDEU!
            \033[0;0m''')
            print(f'\033[36mA palavra sorteada era: {PALAVRA_SECRETA}\033[0;0m')
            menu()
        else:
            opcoes_jogo = [
                inquirer.List(
                    'escolha',
                    message = 'OPÇÕES',
                    choices = ['Pedir dica', 'Chutar letra', 'Sair']
                )
            ]

            print_forca()
            respostas = inquirer.prompt(opcoes_jogo)
            
            if respostas['escolha'] == 'Pedir dica':
                dica(INDICE_SECRET_WORD)
                
            elif respostas['escolha'] == 'Chutar letra':
                chute(PALAVRA_SECRETA)

            elif respostas['escolha'] == 'Sair':
                sair()
            

            
def dica(INDICE_SECRET_WORD):
    acessar_dicas = open(r'./dicas.txt', 'r', encoding='utf-8')
    dicas = acessar_dicas.readlines()
    dica = dicas[INDICE_SECRET_WORD]
    print(f'DICA =', dica)
    

def chute(PALAVRA_SECRETA):
    global LETRAS, CHUTES
    letra = [
        inquirer.List(
            'escolha',
            message = 'TENTATIVA',
            choices = LETRAS
        )
    ]

    respostas = inquirer.prompt(letra)
    CHUTES.append(respostas['escolha'])
    LETRAS.remove(respostas['escolha'])
    
    verificar_letra(respostas['escolha'], PALAVRA_SECRETA)
    print(f'CHUTES: {CHUTES}')


def verificar_letra(letra_escolhida, PALAVRA_SECRETA):
    global TENTATIVAS
    if letra_escolhida in PALAVRA_SECRETA:
        for index, letra in enumerate(PALAVRA_SECRETA):
            if letra_escolhida == letra:
                ANDERLINES_PALAVRA_SECRETA[index] = letra
    else:
        TENTATIVAS -= 1


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
        palavras = open(r'./palavras.txt', 'a', encoding='utf-8')
        palavras.write(f'{palavra}\n')
        palavras.close()
        dicas = open(r'./dicas.txt', 'a', encoding='utf-8')
        dicas.write(f'{dica}\n')
        dicas.close()
        return menu()
    else:
        return add_remove()


def remove():
    print('Qual palavra quer remover? ')
    abrir_palavra = open(r'./palavras.txt', 'r', encoding='utf-8')
    abrir_dicas = open(r'./dicas.txt', 'r', encoding='utf-8')

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

    palavras_file = open(r'./palavras.txt', 'w', encoding='utf-8')
    string_palavras = '\n'.join(lista_palavras)
    palavras_file.write(string_palavras)

    print()
    print(f'\033[1;32mPalavra {respostas} removida com sucesso!\033[0;0m')
    palavras_file.close()


    lista_dicas.pop(indice_palavra)
    dicas_file = open(r'./dicas.txt', 'w', encoding='utf-8')
    string_dicas = '\n'.join(lista_dicas)
    dicas_file.write(string_dicas)
    menu()
  

def view_tips_words():
    print('\033[1;96mPALAVRA\033[0;0m = \033[1;92mDICA\033[0;0m')
    abrir_palavra = open(r'./palavras.txt', 'r', encoding='utf-8')
    abrir_dica = open(r'./dicas.txt', 'r', encoding='utf-8')
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
