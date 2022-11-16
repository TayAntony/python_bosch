import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5 import QtGui
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import QTimer

class Janela(QMainWindow): #Herança
    def __init__(self):
        super().__init__() #Chamando o construtor da classe mãe (QMainWindow)
        self.topo = 100
        self.esquerda = 100
        self.largura = 500
        self.altura = 500
        self.titulo=" Primeira Janela "

        botao1 = QPushButton('Ligar', self)
        botao1.move(10, 10) #posição dentro da janela
        botao1.resize(150, 50)
        botao1.clicked.connect(self.botao1_click)

        botao2 = QPushButton('Desligar', self)
        botao2.move(170, 10) #posição dentro da janela
        botao2.resize(150, 50)
        botao2.clicked.connect(self.botao2_click)

        self.label1 = QLabel(self)
        self.label1.setText("INSIRA UM TEXTO")
        self.label1.move(10, 70)
        self.label1.setStyleSheet('QLabel {font:bold;font-size:20px;color:"blue"}')
        self.label1.resize(200, 20)

        self.imagem = QLabel(self)
        self.imagem.move(10, 100)
        self.imagem.resize(300, 300)
        self.imagem.setScaledContents(True) 
        self.imagem.setPixmap(QtGui.QPixmap('sol.png')) #PARA DIZER QUE VAI SER UMA IMAGEM NÃO UM TEXTO

        self.caixa_texto = QLineEdit(self)
        self.caixa_texto.move(10, 410) 
        self.caixa_texto.resize(150, 25)
        botao_leitura = QPushButton("LEIA", self)
        botao_leitura.move(170, 410)
        botao_leitura.resize(150, 25)
        botao_leitura.clicked.connect(self.leitura)

        self.timer = QTimer()
        self.timer.timeout.connect(self.timeout)

        self.carregar_janela()

    def timeout(self):
        self.label1.setText("Concordo dev")


    def leitura(self):
        texto = self.caixa_texto.text()
        self.caixa_texto.setText("")
        self.label1.setText(texto)
        if self.timer.isActive() == False:
            self.timer.start(3000)
    

    def botao1_click(self):
        print("LIGADO!")
        self.label1.setText("LIGADO")
        self.label1.setStyleSheet('QLabel {font:bold;font-size:20px;color:"green"}')
        self.imagem.setPixmap(QtGui.QPixmap('yuumi_chocada.png'))


    def botao2_click(self):
        print("DESLIGADO!")
        self.label1.setText("DESLIGADO")
        self.label1.setStyleSheet('QLabel {font:bold;font-size:20px;color:"red"}')
        self.imagem.setPixmap(QtGui.QPixmap('yuumi_acordada1.png'))


    def carregar_janela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

if __name__ == "__main__":
    aplicacao = QApplication(sys.argv)
    j= Janela()
    sys.exit(aplicacao.exec())