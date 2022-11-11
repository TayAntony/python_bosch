import sys 
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

janela = QWidget()
janela.setWindowTitle('Minha janela')
janela.setGeometry(0, 0, 300, 200)
label = QLabel('<h4> Olá mundo </h4>', parent=janela)
botao = QPushButton('Printa a gorda', parent=janela)

def meu_botao():
    print('A gorda')

botao.clicked.connect(meu_botao)
botao.move(200,150)
botao.setStyleSheet('background-color: black; color:white; border-radius: 10px; padding: 10px')
janela.setStyleSheet('background-color: purple')
label.setStyleSheet('color: white; font-style: bold')
janela.show()
sys.exit(app.exec_())
