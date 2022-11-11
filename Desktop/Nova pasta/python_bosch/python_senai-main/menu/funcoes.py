import inquirer
import sys


def menu():
    while True:
        perguntas = [
            inquirer.List(
                "escolha",
                message="MENU",
                choices=[
                    "Adicionar novo usuário",
                    "Atualizar Usuário",
                    "Pesquisar Usuário",
                    "Listar Usuários",
                    "Sair",
                ],
            )
        ]
        print("=" * 31)
        print("-=-=-=-=- MENU DA TAY -=-=-=-=-")
        print("=" * 31)
        respostas = inquirer.prompt(perguntas)

        if respostas["escolha"] == "Adicionar novo usuário":
            add_user()

        elif respostas["escolha"] == "Atualizar Usuário":
            update_user()

        elif respostas["escolha"] == "Pesquisar Usuário":
            search_users()

        elif respostas["escolha"] == "Listar Usuários":
            users()

        elif respostas["escolha"] == "Sair":
            sair()
            sys.exit()


def add_user():
    while True:
        nome = input("Digite seu nome completo: ").upper().strip()
        print("-" * 50)
        print(f"NOME = {nome}\n")
        users = open(r"./menu/usuarios.txt", "r", encoding="utf-8")
        cadastros = users.readlines()
        usuario_existe = False

        for cadastro in cadastros:
            separando = cadastro.split("\n")

            if separando[0].strip() == nome:
                print("\033[1;31mUsuário já cadastrado\33[m")
                usuario_existe = True

        if usuario_existe:
            continue

        else:
            confirmar = input("As informações estão corretas? [S/N] ").upper().strip()
            if confirmar == "S":
                print("\33[32mCADASTRO EFETUADO COM SUCESSO \33[m")
                cadastros = open(r"./menu/usuarios.txt", "a", encoding="utf-8")
                cadastros.write(f"{nome}\n")
                cadastros.close()
                break
            else:
                return add_user()
    menu()


def update_user():
    pesquisa = input("Digite o usuário que quer pesquisar: ").upper().strip()
    users = open(r"./menu/usuarios.txt", "r", encoding="utf-8")
    cadastros = users.readlines()

    lista_nomes = []
    resultado_pesquisa = []

    for cadastro in cadastros:
        lista_nomes.append(cadastro.split("\n"))

    for nome_completo in lista_nomes:
        if pesquisa in nome_completo[0]:
            resultado_pesquisa.append(*nome_completo[:-1])

    if len(resultado_pesquisa) == 0:
        print("\033[1;31mUsuário não encontrado :/\33[m")
    else:
        pessoas = [
            inquirer.List(
                "escolha", message="Usuários encontrados", choices=resultado_pesquisa
            )
        ]
        usuario_a_atualizar = inquirer.prompt(pessoas)["escolha"]

        for index, usuario in enumerate(cadastros):
            if usuario_a_atualizar + "\n" == usuario:
                novo_nome = (
                    input(f"Digite o novo nome do usuário {usuario_a_atualizar}: ")
                    .upper()
                    .strip()
                )
                cadastros[index] = novo_nome + "\n"

        string_cadastros = "".join(cadastros)

        arquivo_usuarios = open(r"./menu/usuarios.txt", "w", encoding="utf-8")
        arquivo_usuarios.write(string_cadastros)
        arquivo_usuarios.close()

        print("\33[32mUsuário atualizado com sucesso.\33[m")


def search_users():
    pesquisa = input("Digite o usuário que quer pesquisar: ").upper().strip()
    users = open(r"./menu/usuarios.txt", "r", encoding="utf-8")
    lista_nomes = []
    cadastros = users.readlines()

    for cadastro in cadastros:
        lista_nomes.append(cadastro[0:].split(" "))
    acumulador = 0

    for nome_completo in lista_nomes:
        if pesquisa in nome_completo[0]:
            print(f"Usuário:", *nome_completo[:-1])
            acumulador += 1
    if acumulador == 0:
        print("\033[1;31mUsuário não encontrado :/\33[m")


def users():
    users = open(r"./menu/usuarios.txt", "r", encoding="utf-8")
    cadastros = users.readlines()

    lista_nomes = []

    for cadastro in cadastros:
        lista_nomes.append(cadastro.split("\n"))

    pessoas = [
        inquirer.List("escolha", message="Usuários cadastrados", choices=lista_nomes)
    ]

    respostas = inquirer.prompt(pessoas)
    if respostas["escolha"] == "":
        menu()


def sair():
    print("\033[1;35mAté a próxima DEV \U0001F47E\33[m")
