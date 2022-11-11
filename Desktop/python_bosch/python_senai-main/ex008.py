from time import sleep
import pyautogui

pyautogui.PAUSE = .5

pyautogui.moveTo(550,570,2)
pyautogui.click()
pyautogui.typewrite("5")
pyautogui.press('enter')
pyautogui.click()
pyautogui.typewrite("6.4")
pyautogui.press('enter')


n1 = float(input('Digite o valor da primeira nota: '))
n2 = float(input('Digite o valor da segunda nota: '))

media = (n1+n2)/2
print(f'A média é {media}')
print('Situação do aluno: ', end='')
sleep(1)
if media > 7.0:
    print('APROVADO')
elif media >= 5 and media <=6.9:
    print('REGULAR')
elif media >3.1 and media <4.9:
    print('RECUPERAÇÃO')
elif media <=3:
    print('REPROVADO')
