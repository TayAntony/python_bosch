import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5 import QtGui
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import QTimer
from random import randint

class Janela(QMainWindow): #Herança
    def __init__(self):
        super().__init__() #Chamando o construtor da classe mãe (QMainWindow)
        self.topo = 200
        self.esquerda = 700
        self.largura = 600
        self.altura = 700
        self.forma_usuario = 'X'
        self.forma_pc = 'O'
        self.placar_usuario = 0
        self.placar_pc = 0
        self.placar_velha = 0
        self.vez = 'jogador1'
        self.titulo="JOGO DA VELHA"
        self.botao_a1_bool = False
        self.botao_a2_bool = False
        self.botao_a3_bool = False
        self.botao_b1_bool = False
        self.botao_b2_bool = False
        self.botao_b3_bool = False
        self.botao_c1_bool = False
        self.botao_c2_bool = False
        self.botao_c3_bool = False

        self.boas_vindas = QLabel(self)
        self.boas_vindas.setText("Seja bem vindo ao meu jogo!")
        self.boas_vindas.move(80, 10)
        self.boas_vindas.resize(450, 50)
        self.boas_vindas.setStyleSheet('QLabel {font:bold;font-size:30px;color:"purple"}')
    
        self.imagem = QLabel(self)
        self.imagem.move(130, 100)
        self.imagem.resize(350, 300)
        self.imagem.setScaledContents(True) 
        self.imagem.setPixmap(QtGui.QPixmap('imagens/velha.png'))

        self.botao_play = QPushButton("PLAY", self)
        self.botao_play.move(220, 450)
        self.botao_play.resize(140, 60)
        self.botao_play.setStyleSheet('QPushButton {font:30px bold; color: "black"; border:2px solid black; background: "white"; border-radius:10px} QPushButton:hover{background:"black"; color:"white"}')
        self.botao_play.clicked.connect(self.play_botao)

        self.botao_sair = QPushButton("SAIR DO JOGO", self)
        self.botao_sair.move(500, 5)
        self.botao_sair.resize(85, 20)
        self.botao_sair.setStyleSheet('QPushButton {font:10px; color: "red"; border:2px solid red; background: "white"; border-radius:10px} QPushButton:hover{background:"red"; color:"white"; font:bold}')
        self.botao_sair.clicked.connect(self.sair)
        self.botao_sair.hide()

        self.usuario_joga = QLabel(self)
        self.usuario_joga.move(70, 20)
        self.usuario_joga.resize(250, 40)
        self.usuario_joga.setStyleSheet('QLabel {color: "blue"; font: 30px}')
        self.usuario_joga.setText("Jogador 1: "+ self.forma_usuario)
        self.usuario_joga.hide()

        self.pc_joga = QLabel(self)
        self.pc_joga.move(70, 70)
        self.pc_joga.resize(250, 40)
        self.pc_joga.setStyleSheet('QLabel {color: "red"; font: 30px}')
        self.pc_joga.setText("Jogador 2: "+ self.forma_pc)
        self.pc_joga.hide()

        self.lbl_vencedor = QLabel(self)
        self.lbl_vencedor.move(350, 50)
        self.lbl_vencedor.resize(250, 40)
        self.lbl_vencedor.setStyleSheet('QLabel {color: "green"; font: 30px}')
        self.lbl_vencedor.setText("Vencedor: ")
        self.lbl_vencedor.hide()

        self.imagem_vencedor_usuario = QLabel(self)
        self.imagem_vencedor_usuario.move(490, 30)
        self.imagem_vencedor_usuario.resize(100, 100)
        self.imagem_vencedor_usuario.setScaledContents(True) 
        self.imagem_vencedor_usuario.setPixmap(QtGui.QPixmap('imagens/player1.png'))
        self.imagem_vencedor_usuario.hide()

        self.imagem_vencedor_pc = QLabel(self)
        self.imagem_vencedor_pc.move(490, 30)
        self.imagem_vencedor_pc.resize(100, 80)
        self.imagem_vencedor_pc.setScaledContents(True) 
        self.imagem_vencedor_pc.setPixmap(QtGui.QPixmap('imagens/twitch.png'))
        self.imagem_vencedor_pc.hide()

        self.imagem_vencedor_velha = QLabel(self)
        self.imagem_vencedor_velha.move(510, 40)
        self.imagem_vencedor_velha.resize(70, 70)
        self.imagem_vencedor_velha.setScaledContents(True) 
        self.imagem_vencedor_velha.setPixmap(QtGui.QPixmap('imagens/velha.png'))
        self.imagem_vencedor_velha.hide() 

        self.linha_vertical1 = QLabel(self)
        self.linha_vertical1.move(220, 150)
        self.linha_vertical1.resize(10, 400)
        self.linha_vertical1.setStyleSheet('QLabel {background: "black"}')
        self.linha_vertical1.hide()

        self.linha_vertical2 = QLabel(self)
        self.linha_vertical2.move(380, 150)
        self.linha_vertical2.resize(10, 400)
        self.linha_vertical2.setStyleSheet('QLabel {background: "black"}')
        self.linha_vertical2.hide()

        self.linha_horizontal1 = QLabel(self)
        self.linha_horizontal1.move(70, 280)
        self.linha_horizontal1.resize(460, 10)
        self.linha_horizontal1.setStyleSheet('QLabel {background: "black"}')
        self.linha_horizontal1.hide()

        self.linha_horizontal2 = QLabel(self)
        self.linha_horizontal2.move(70, 420)
        self.linha_horizontal2.resize(460, 10)
        self.linha_horizontal2.setStyleSheet('QLabel {background: "black"}')
        self.linha_horizontal2.hide()

        self.botao_a1 = QPushButton("", self)
        self.botao_a1.move(90, 150)
        self.botao_a1.resize(120, 120)
        self.botao_a1.setStyleSheet('QPushButton {font:100px bold; color: "blue"; border:2px solid white; background: "white"; border-radius:10px;}')
        self.botao_a1.clicked.connect(lambda : self.escolha_usuario(1))
        self.botao_a1.hide()

        self.botao_a2 = QPushButton("", self)
        self.botao_a2.move(245, 150)
        self.botao_a2.resize(120, 120)
        self.botao_a2.setStyleSheet('QPushButton {font:100px bold; color: "blue"; border:2px solid white; background: "white"; border-radius:10px;}')
        self.botao_a2.clicked.connect(lambda : self.escolha_usuario(2))
        self.botao_a2.hide()

        self.botao_a3 = QPushButton("", self)
        self.botao_a3.move(400, 150)
        self.botao_a3.resize(120, 120)
        self.botao_a3.setStyleSheet('QPushButton {font:100px bold; color: "blue"; border:2px solid white; background: "white"; border-radius:10px;}')
        self.botao_a3.clicked.connect(lambda : self.escolha_usuario(3))
        self.botao_a3.hide()

        self.botao_b1 = QPushButton("", self)
        self.botao_b1.move(90, 295)
        self.botao_b1.resize(120, 120)
        self.botao_b1.setStyleSheet('QPushButton {font:100px bold; color: "blue"; border:2px solid white; background: "white"; border-radius:10px;}')
        self.botao_b1.clicked.connect(lambda : self.escolha_usuario(4))
        self.botao_b1.hide()

        self.botao_b2 = QPushButton("", self)
        self.botao_b2.move(245, 295)
        self.botao_b2.resize(120, 120)
        self.botao_b2.setStyleSheet('QPushButton {font:100px bold; color: "blue"; border:2px solid white; background: "white"; border-radius:10px;}')
        self.botao_b2.clicked.connect(lambda : self.escolha_usuario(5))
        self.botao_b2.hide()

        self.botao_b3 = QPushButton("", self)
        self.botao_b3.move(400, 295)
        self.botao_b3.resize(120, 120)
        self.botao_b3.setStyleSheet('QPushButton {font:100px bold; color: "blue"; border:2px solid white; background: "white"; border-radius:10px;}')
        self.botao_b3.clicked.connect(lambda : self.escolha_usuario(6))
        self.botao_b3.hide()

        self.botao_c1 = QPushButton("", self)
        self.botao_c1.move(90, 435)
        self.botao_c1.resize(120, 120)
        self.botao_c1.setStyleSheet('QPushButton {font:100px bold; color: "blue"; border:2px solid white; background: "white"; border-radius:10px;}')
        self.botao_c1.clicked.connect(lambda : self.escolha_usuario(7))
        self.botao_c1.hide()

        self.botao_c2 = QPushButton("", self)
        self.botao_c2.move(245, 435)
        self.botao_c2.resize(120, 120)
        self.botao_c2.setStyleSheet('QPushButton {font:100px bold; color: "blue"; border:2px solid white; background: "white"; border-radius:10px;}')
        self.botao_c2.clicked.connect(lambda : self.escolha_usuario(8))
        self.botao_c2.hide()

        self.botao_c3 = QPushButton("", self)
        self.botao_c3.move(400, 435)
        self.botao_c3.resize(120, 120)
        self.botao_c3.setStyleSheet('QPushButton {font:100px bold; color: "blue"; border:2px solid white; background: "white"; border-radius:10px;}')
        self.botao_c3.clicked.connect(lambda : self.escolha_usuario(9))
        self.botao_c3.hide()


        self.img_usuario = QLabel(self)
        self.img_usuario.move(100, 600)
        self.img_usuario.resize(60, 60)
        self.img_usuario.setScaledContents(True)
        self.img_usuario.setPixmap(QtGui.QPixmap('imagens/player1.png'))
        self.img_usuario.hide()

        self.img_pc = QLabel(self)
        self.img_pc.move(270, 605)
        self.img_pc.resize(60, 50)
        self.img_pc.setScaledContents(True)
        self.img_pc.setPixmap(QtGui.QPixmap('imagens/twitch.png'))
        self.img_pc.hide()

        self.img_velha = QLabel(self)
        self.img_velha.move(440, 600)
        self.img_velha.resize(50, 50)
        self.img_velha.setScaledContents(True)
        self.img_velha.setPixmap(QtGui.QPixmap('imagens/velha.png'))
        self.img_velha.hide()

        self.lbl_placar_usuario = QLabel(self)
        self.lbl_placar_usuario.setText(str(self.placar_usuario))
        self.lbl_placar_usuario.move(70, 620)
        self.lbl_placar_usuario.resize(30, 30)
        self.lbl_placar_usuario.setStyleSheet('QLabel {color: "blue"; font: 30px}')
        self.lbl_placar_usuario.hide()

        self.lbl_placar_pc = QLabel(self)
        self.lbl_placar_pc.setText(str(self.placar_pc))
        self.lbl_placar_pc.move(230, 620)
        self.lbl_placar_pc.resize(30, 30)
        self.lbl_placar_pc.setStyleSheet('QLabel {color: "red"; font: 30px}')
        self.lbl_placar_pc.hide()

        self.lbl_placar_velha = QLabel(self)
        self.lbl_placar_velha.setText(str(self.placar_velha))
        self.lbl_placar_velha.move(400, 620)
        self.lbl_placar_velha.resize(30, 30)
        self.lbl_placar_velha.setStyleSheet('QLabel {color: "grey"; font: 30px}')
        self.lbl_placar_velha.hide()

        self.botao_resetar = QPushButton("RESETAR JOGO", self)
        self.botao_resetar.move(400, 5)
        self.botao_resetar.resize(95, 20)
        self.botao_resetar.setStyleSheet('QPushButton {font:12px bold; color: "green"; border:2px solid green; background: "white"; border-radius:10px;} QPushButton:hover{background:"green"; color:"white"; font: bold}')
        self.botao_resetar.clicked.connect(self.resetar_jogo)
        self.botao_resetar.hide()

        self.carregar_janela()

    def play_botao(self):
        self.boas_vindas.hide()
        self.imagem.hide()
        self.imagem.hide()
        self.botao_play.hide()
        self.botao_sair.show()
        self.linha_vertical1.show()
        self.linha_vertical2.show()
        self.linha_horizontal1.show()
        self.linha_horizontal2.show()
        self.botao_a1.show()
        self.botao_a2.show()
        self.botao_a3.show()
        self.botao_b1.show()
        self.botao_b2.show()
        self.botao_b3.show()
        self.botao_c1.show()
        self.botao_c2.show()
        self.botao_c3.show()
        self.lbl_placar_usuario.show()
        self.lbl_placar_pc.show()
        self.lbl_placar_velha.show()
        self.img_usuario.show()
        self.img_pc.show()
        self.img_velha.show()
        self.pc_joga.show()
        self.usuario_joga.show()
        self.lbl_vencedor.show()
        self.botao_resetar.show()
    

    def escolha_usuario(self, botao):
        if self.vez == 'jogador1':
            if botao == 1:
                self.botao_a1.setText("X")
                self.botao_a1.setDisabled(True)
                self.vez = 'jogador2'
                self.botao_a1_bool = True
                self.botao_a1.setStyleSheet('QPushButton {font:100px bold; color: "blue"; border:2px solid white; background: "white"; border-radius:10px;}')
            elif botao == 2:
                self.botao_a2.setText("X")
                self.botao_a2.setDisabled(True)
                self.vez = 'jogador2'
                self.botao_a2_bool = True
                self.botao_a2.setStyleSheet('QPushButton {font:100px bold; color: "blue"; border:2px solid white; background: "white"; border-radius:10px;}')
            elif botao == 3:
                self.botao_a3.setText("X")
                self.botao_a3.setDisabled(True)
                self.vez = 'jogador2'
                self.botao_a3_bool = True
                self.botao_a3.setStyleSheet('QPushButton {font:100px bold; color: "blue"; border:2px solid white; background: "white"; border-radius:10px;}')
            elif botao == 4:
                self.botao_b1.setText("X")
                self.botao_b1.setDisabled(True)
                self.vez = 'jogador2'
                self.botao_b1_bool = True
                self.botao_b1.setStyleSheet('QPushButton {font:100px bold; color: "blue"; border:2px solid white; background: "white"; border-radius:10px;}')
            elif botao == 5:
                self.botao_b2.setText("X")
                self.botao_b2.setDisabled(True)
                self.vez = 'jogador2'
                self.botao_b2_bool = True
                self.botao_b2.setStyleSheet('QPushButton {font:100px bold; color: "blue"; border:2px solid white; background: "white"; border-radius:10px;}')
            elif botao == 6:
                self.botao_b3.setText("X")
                self.botao_b3.setDisabled(True)
                self.vez = 'jogador2'
                self.botao_b3_bool = True
                self.botao_b3.setStyleSheet('QPushButton {font:100px bold; color: "blue"; border:2px solid white; background: "white"; border-radius:10px;}')
            elif botao == 7:
                self.botao_c1.setText("X")
                self.botao_c1.setDisabled(True)
                self.vez = 'jogador2'
                self.botao_c1_bool = True
                self.botao_c1.setStyleSheet('QPushButton {font:100px bold; color: "blue"; border:2px solid white; background: "white"; border-radius:10px;}')
            elif botao == 8:
                self.botao_c2.setText("X")
                self.botao_c2.setDisabled(True)
                self.vez = 'jogador2'
                self.botao_c2_bool = True
                self.botao_c2.setStyleSheet('QPushButton {font:100px bold; color: "blue"; border:2px solid white; background: "white"; border-radius:10px;}')
            elif botao == 9:
                self.botao_c3.setText("X")
                self.botao_c3.setDisabled(True)
                self.vez = 'jogador2'
                self.botao_c3_bool = True
                self.botao_c3.setStyleSheet('QPushButton {font:100px bold; color: "blue"; border:2px solid white; background: "white"; border-radius:10px;}')
            
            if self.verificar_vencedor_x():
                self.placar_usuario += 1
                self.lbl_placar_usuario.setText(str(self.placar_usuario))
                self.imagem_vencedor_usuario.show()
                self.botao_a1.setDisabled(True)
                self.botao_a2.setDisabled(True)
                self.botao_a3.setDisabled(True)
                self.botao_b1.setDisabled(True)
                self.botao_b2.setDisabled(True)
                self.botao_b3.setDisabled(True)
                self.botao_c1.setDisabled(True)
                self.botao_c2.setDisabled(True)
                self.botao_c3.setDisabled(True)
            else:
                if self.botao_a1_bool == True and self.botao_a2_bool == True and self.botao_a3_bool == True and self.botao_b1_bool == True and self.botao_b2_bool == True and self.botao_b3_bool == True and self.botao_c1_bool == True and self.botao_c2_bool == True and self.botao_c3_bool == True:
                    self.verificar_velha()

        else:
            if botao == 1:
                self.botao_a1.setText("O")
                self.botao_a1.setDisabled(True)
                self.vez = 'jogador1'
                self.botao_a1_bool = True
                self.botao_a1.setStyleSheet('QPushButton {font:100px bold; color: "red"; border:2px solid white; background: "white"; border-radius:10px;}')
            elif botao == 2:
                self.botao_a2.setText("O")
                self.botao_a2.setDisabled(True)
                self.vez = 'jogador1'
                self.botao_a2_bool = True
                self.botao_a2.setStyleSheet('QPushButton {font:100px bold; color: "red"; border:2px solid white; background: "white"; border-radius:10px;}')
            elif botao == 3:
                self.botao_a3.setText("O")
                self.botao_a3.setDisabled(True)
                self.vez = 'jogador1'
                self.botao_a3_bool = True
                self.botao_a3.setStyleSheet('QPushButton {font:100px bold; color: "red"; border:2px solid white; background: "white"; border-radius:10px;}')
            elif botao == 4:
                self.botao_b1.setText("O")
                self.botao_b1.setDisabled(True)
                self.vez = 'jogador1'
                self.botao_b1_bool = True
                self.botao_b1.setStyleSheet('QPushButton {font:100px bold; color: "red"; border:2px solid white; background: "white"; border-radius:10px;}')
            elif botao == 5:
                self.botao_b2.setText("O")
                self.botao_b2.setDisabled(True)
                self.vez = 'jogador1'
                self.botao_b2_bool = True
                self.botao_b2.setStyleSheet('QPushButton {font:100px bold; color: "red"; border:2px solid white; background: "white"; border-radius:10px;}')
            elif botao == 6:
                self.botao_b3.setText("O")
                self.botao_b3.setDisabled(True)
                self.vez = 'jogador1'
                self.botao_b3_bool = True
                self.botao_b3.setStyleSheet('QPushButton {font:100px bold; color: "red"; border:2px solid white; background: "white"; border-radius:10px;}')
            elif botao == 7:
                self.botao_c1.setText("O")
                self.botao_c1.setDisabled(True)
                self.vez = 'jogador1'
                self.botao_c1_bool = True
                self.botao_c1.setStyleSheet('QPushButton {font:100px bold; color: "red"; border:2px solid white; background: "white"; border-radius:10px;}')
            elif botao == 8:
                self.botao_c2.setText("O")
                self.botao_c2.setDisabled(True)
                self.vez = 'jogador1'
                self.botao_c2_bool = True
                self.botao_c2.setStyleSheet('QPushButton {font:100px bold; color: "red"; border:2px solid white; background: "white"; border-radius:10px;}')
            elif botao == 9:
                self.botao_c3.setText("O")
                self.botao_c3.setDisabled(True)
                self.vez = 'jogador1'
                self.botao_c3_bool = True
                self.botao_c3.setStyleSheet('QPushButton {font:100px bold; color: "red"; border:2px solid white; background: "white"; border-radius:10px;}')  
            
            if self.verificar_vencedor_o():
                self.placar_pc += 1
                self.lbl_placar_pc.setText(str(self.placar_pc))
                self.imagem_vencedor_pc.show()
                self.botao_a1.setDisabled(True)
                self.botao_a2.setDisabled(True)
                self.botao_a3.setDisabled(True)
                self.botao_b1.setDisabled(True)
                self.botao_b2.setDisabled(True)
                self.botao_b3.setDisabled(True)
                self.botao_c1.setDisabled(True)
                self.botao_c2.setDisabled(True)
                self.botao_c3.setDisabled(True)
            else: 
                if self.botao_a1_bool == True and self.botao_a2_bool == True and self.botao_a3_bool == True and self.botao_b1_bool == True and self.botao_b2_bool == True and self.botao_b3_bool == True and self.botao_c1_bool == True and self.botao_c2_bool == True and self.botao_c3_bool == True:
                    self.verificar_velha()


    def verificar_vencedor_x(self):
        if self.botao_a1.text() == "X" and self.botao_a2.text() == "X" and self.botao_a3.text() == "X":
            return True
        elif self.botao_b1.text() == "X" and self.botao_b2.text()  == "X" and self.botao_b3.text() == "X":
            return True
        elif self.botao_c1.text() == "X" and self.botao_c2.text() == "X" and self.botao_c3.text() == "X":
            return True
        elif self.botao_a1.text() == "X" and self.botao_b1.text() == "X" and self.botao_c1.text() == "X":
            return True
        elif self.botao_a2.text() == "X" and self.botao_b2.text() == "X" and self.botao_c2.text() == "X":
            return True
        elif self.botao_a3.text() == "X" and self.botao_b3.text() == "X" and self.botao_c3.text() == "X":
            return True
        elif self.botao_a1.text() == "X" and self.botao_b2.text() == "X" and self.botao_c3.text() == "X":
            return True
        elif self.botao_a3.text() == "X" and self.botao_b2.text() == "X" and self.botao_c1.text() == "X":
            return True
        else:
            return False


    def verificar_vencedor_o(self):
        if self.botao_a1.text() == "O" and self.botao_a2.text() == "O" and self.botao_a3.text() == "O":
            return True
        elif self.botao_b1.text() == "O" and self.botao_b2.text()  == "O" and self.botao_b3.text() == "O":
            return True
        elif self.botao_c1.text() == "O" and self.botao_c2.text() == "O" and self.botao_c3.text() == "O":
            return True
        elif self.botao_a1.text() == "O" and self.botao_b1.text() == "O" and self.botao_c1.text() == "O":
            return True
        elif self.botao_a2.text() == "O" and self.botao_b2.text() == "O" and self.botao_c2.text() == "O":
            return True
        elif self.botao_a3.text() == "O" and self.botao_b3.text() == "O" and self.botao_c3.text() == "O":
            return True
        elif self.botao_a1.text() == "O" and self.botao_b2.text() == "O" and self.botao_c3.text() == "O":
            return True
        elif self.botao_a3.text() == "O" and self.botao_b2.text() == "O" and self.botao_c1.text() == "O":
            return True
        else:
            return False

    def verificar_velha(self):
        self.placar_velha += 1
        self.lbl_placar_velha.setText(str(self.placar_velha))
        self.imagem_vencedor_velha.show()

    def resetar_jogo(self):
            self.vez = 'jogador1'
            self.botao_a1.setDisabled(False)
            self.botao_a2.setDisabled(False)
            self.botao_a3.setDisabled(False)
            self.botao_b1.setDisabled(False)
            self.botao_b2.setDisabled(False)
            self.botao_b3.setDisabled(False)
            self.botao_c1.setDisabled(False)
            self.botao_c2.setDisabled(False)
            self.botao_c3.setDisabled(False)

            self.botao_a1.setText("")
            self.botao_a2.setText("")
            self.botao_a3.setText("")
            self.botao_b1.setText("")
            self.botao_b2.setText("")
            self.botao_b3.setText("")
            self.botao_c1.setText("")
            self.botao_c2.setText("")
            self.botao_c3.setText("")

            self.botao_a1_bool = False
            self.botao_a2_bool = False
            self.botao_a3_bool = False
            self.botao_b1_bool = False
            self.botao_b2_bool = False
            self.botao_b3_bool = False
            self.botao_c1_bool = False
            self.botao_c2_bool = False
            self.botao_c3_bool = False

            self.imagem_vencedor_usuario.hide()
            self.imagem_vencedor_pc.hide()
            self.imagem_vencedor_velha.hide()
        

    def sair(self):
        sys.exit()

    def carregar_janela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.setStyleSheet('background: "white"')
        self.show()

if __name__ == "__main__":
    aplicacao = QApplication(sys.argv)
    j= Janela()
    sys.exit(aplicacao.exec())
