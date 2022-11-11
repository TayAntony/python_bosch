import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

janela = QWidget()
janela.setWindowTitle('Minha janela')
janela.setGeometry(0, 0, 500, 500)
label = QLabel('<h4> Olá mundo </h4>', parent=janela)
botao = QPushButton('Clique aqui!', parent=janela)

def meu_botao():
    print('Oi Programador')

    botao.setStyleSheet('background-color: white; color:black; border-radius: 20px; padding: 10px; font-weight: bold')
    botao.move(250,300)

    botao.setStyleSheet('background-color: pink; color:black; border-radius: 20px; padding: 10px; font-weight: bold')
    botao.move(100,250)

    botao.setStyleSheet('background-color: orange; color:black; border-radius: 20px; padding: 10px; font-weight: bold')
    botao.move(150,400)

botao.clicked.connect(meu_botao)
botao.move(350,400)
botao.setStyleSheet('background-color: blue; color:white; border-radius: 20px; padding: 20px')
janela.setStyleSheet('background-color: grey')
label.setStyleSheet('color: white; font-style: bold; text-align: center;')
janela.show()
sys.exit(app.exec_())
