from random import randint
from time import sleep
import sys

def regra():
    print('\033[1;34m=-=-=-=-=-=-=-=-=- JOGO DE ADIVINHAÇÃO -=-=-=-=-=-=-=-=-=-= \033[0;0m')
    print('AS REGRAS SÃO:')
    sleep(0.5)
    print('>>> VOU PENSAR EM UM NÚMERO DE 0 A 100')
    sleep(1.5)
    print('>>> VOCÊ TEM 3 CHUTES E 50 DE VIDA')
    sleep(1.5)
    print('>>> O SEU CHUTE E SUA QUANTIDADE DE VIDA SÃO RELACIONAIS...')
    sleep(1.5)
    print('\033[1;36m>>> BOA SORTE PLAYER\033[0;0m')
    sleep(1.5)
    aleatorio()


def aleatorio():
    num_computador = randint(0,100)
    vida = 50
    chutes = 3
    print('\033[1;32mSUA VIDA ATUAL É 50')
    print('Você tem 3 chutes\033[0;0m')

    while chutes > 0:
        while True:
            n = input('Digite um número entre 0 e 100 para chutar: ').strip()
            try:
                n = int(n)
                if n < 0 or n > 100:
                    print('\033[1;31mVocê não digitou um número entre 0 e 100!\033[0;0m')
                    continue
                break
            except:
                print('\033[1;31mVocê não digitou um número!\033[0;0m')

        if n > num_computador:
            print(f'\033[1;93mO número sorteado é MENOR que {n}\033[0;0m')
            print('=-=-'*14)
            chutes-=1

            calculo_vida = n-num_computador
            vida = vida-calculo_vida

            if vida == 0 or vida < 0:
                print(f'\033[1;91mInfelizmente seus pontos de vida zeraram, o número sorteado era: {num_computador}\033[0;0m')
                parada = novamente()
                if parada == 'parada':
                    break
            else:
                print(f'Você tem {vida} pontos de vida e {chutes} chute(s)')

        elif n < num_computador:
            print(f'\033[1;93mO número sorteado é MAIOR que {n}\033[0;0m')
            print('=-=-'*14)
            chutes-=1
            calculo_vida = num_computador-n
            vida = vida - calculo_vida
            if vida == 0 or vida < 0:
                print(f'\033[1;91mInfelizmente seus pontos de vida zeraram, o número sorteado era: {num_computador}\033[0;0m')
                parada = novamente()
                if parada == 'parada':
                    break
            else:
                print(f'Você tem {vida} pontos de vida e {chutes} chute(s)')

        else:
            print(f'\033[1;35mParabéns, você ganhou! O número sorteado era {num_computador}\033[0;0m')
            parada = novamente()
            if parada == 'parada':
                break
           
        if chutes == 0:
            print(f'\033[1;91mInfelizmente seus chutes acabaram, o número sorteado era: {num_computador}\033[0;0m')
            parada = novamente()
            if parada == 'parada':
                break

def novamente():
    while True:
        again = input('\033[1;92mDeseja continuar? [S/N]: \033[0;0m').lower().strip()[0]
        if again == 's' or again == 'n':
            if again == 's':
                
                while True:
                    regras = input('Deseja ler as regras novamente? [S/N]: ').lower().strip()[0]
                    if regras == 's' or regras == 'n':
                        if regras == 's':
                            regra()
                        else:
                            aleatorio()
                    else:
                        print('\033[1;31mVocê não digitou Sim ou Não\033[0;0m')
                        continue
            else:
                sys.exit('\033[1;30m\033[1;107mAté a próxima Dev \033[0;0m👾')
        else:
            print('\033[1;31mVocê não digitou Sim ou Não\033[0;0m')
            continue

if __name__ == '__main__':
    regra()