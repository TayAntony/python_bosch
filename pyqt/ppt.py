import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5 import QtGui
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import QTimer

class Janela(QMainWindow): #Herança
    def __init__(self):
        super().__init__() #Chamando o construtor da classe mãe (QMainWindow)
        self.topo = 200
        self.esquerda = 200
        self.largura = 900
        self.altura = 500
        self.titulo="ROCK, PAPERS, SCISSORS"

        self.start = QPushButton('PLAY', self)
        self.start.move(350, 400)
        self.start.resize(200, 50)
        self.start.setStyleSheet('QPushButton {font:30px bold; color: "white"; border:2px solid white; background: "black"; border-radius:10px;} QPushButton:hover{background:"white"; color:"black"}')
        self.start.clicked.connect(self.start_click)

        self.imagem = QLabel(self)
        self.imagem.move(50, 50)
        self.imagem.resize(800, 300)
        self.imagem.setScaledContents(True) 
        self.imagem.setPixmap(QtGui.QPixmap('pedpaptes.png')) #PARA DIZER QUE VAI SER UMA IMAGEM NÃO UM TEXTO

        self.label1 = QLabel(self)
        self.label1.move(120,100)
        self.label1.resize(650, 50)
        self.label1.setText("  <<<<<<< SEJA BEM-VINDO(A) AO JOGO! >>>>>>>")
        self.label1.setStyleSheet('QLabel {background: "white"; font:25px; color:"grey"}')
        self.label1.hide()

        self.label_regras = QLabel(self)
        self.label_regras.move(190,200)
        self.label_regras.resize(500, 250)
        self.label_regras.setText(""" AS REGRAS SÃO AS SEGUINTES:
    - O COMPUTADOR VAI JOGAR PRIMEIRO E VOCÊ 
    TERÁ 1 SEGUNDO PARA REVIDAR

    - PARTIDA DURARÁ 10 SEGUNDOS, TENTE 
    GANHAR O MÁXIMO NESSE PERÍODO

    - SE VOCÊ NÃO JOGAR EM 1 SEGUNDO O 
    COMPUTADOR GANHA
        """)
        self.label_regras.setStyleSheet('QLabel {background: "white"; font:20px; color:"black"}')
        self.label_regras.hide()

        
        self.caixa_texto = QLineEdit(self)
        self.caixa_texto.move(300, 200)
        self.caixa_texto.resize(300, 50)
        self.caixa_texto.hide()
        
        self.carregar_janela()
    

    def start_click(self):
        print("DEU PLAY")
        self.start.hide()
        self.imagem.hide()
        self.label1.show()
        self.label_regras.show()
        

    def carregar_janela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.setStyleSheet('background: "black"')
        self.show()


if __name__ == "__main__":
    aplicacao = QApplication(sys.argv)
    j= Janela()
    sys.exit(aplicacao.exec())