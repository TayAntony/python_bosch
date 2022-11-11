from random import choice
print('-=-' *26)
print(f'Estou pensando em um número de 0 a 5... Tente adivinhar:')
print('-=-' *26)

while True:
    again = input('Deseja tentar? [S/N] ').upper().strip()
    if again == 'S':
        tentativa = int(input('Digite sua tentativa: '))
        lista = [1,5]
        escolha = choice(lista)
        if tentativa == escolha:
            print(f'Meus parabéns, você acertou!', end='')
            print('\U0001F929')
        else:
            print(f'Que pena, você errou. Eu pensei no número {escolha}! Mais sorte na próxima', end='')
            print("\U0001F97A")
    else:
        print('Volte sempre! ', end='')
        print('\U0001F496')
        break
