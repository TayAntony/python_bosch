import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer
from random import randint

def iniciar():
    j = Janela()
    

class Janela(QMainWindow):  # Herança
    def __init__(self):
        super().__init__()  # Chamando o construtor da classe mãe (QMainWindow)
        self.topo = 200
        self.esquerda = 200
        self.largura = 900
        self.altura = 500
        self.titulo = "ROCK, PAPER, SCISSORS"
        self.contador_valor = 3
        self.main_timer_10 = 10
        self.iniciou = False
        self.iniciou_main_timer = False
        self.placar_jogador = 0
        self.placar_computador = 0
        self.placar_empate = 0
        self.jogada_usuario = "Demorou"
        self.primeira_vez = True

        self.start = QPushButton("PLAY", self)
        self.start.move(350, 400)
        self.start.resize(200, 50)
        self.start.setStyleSheet(
            'QPushButton {font:30px bold; color: "white"; border:2px solid white; background: "black"; border-radius:10px;} QPushButton:hover{background:"white"; color:"black"}'
        )
        self.start.clicked.connect(self.start_click)

        self.imagem = QLabel(self)
        self.imagem.move(50, 50)
        self.imagem.resize(800, 300)
        self.imagem.setScaledContents(True)
        self.imagem.setPixmap(
            QtGui.QPixmap("imagens_ppt/pedpaptes.png")
        )  # PARA DIZER QUE VAI SER UMA IMAGEM NÃO UM TEXTO

        self.label1 = QLabel(self)
        self.label1.move(190, 50)
        self.label1.resize(500, 50)
        self.label1.setText("      < SEJA BEM-VINDO(A) AO JOGO! >")
        self.label1.setStyleSheet(
            'QLabel {background: "white"; font:25px; color:"black";border:1px solid black; border-radius:10px}'
        )
        self.label1.hide()

        self.label_regras = QLabel(self)
        self.label_regras.move(190, 100)
        self.label_regras.resize(500, 250)
        self.label_regras.setText(
            """ AS REGRAS SÃO AS SEGUINTES:
    - O COMPUTADOR VAI JOGAR PRIMEIRO E VOCÊ 
    TERÁ 1 SEGUNDO PARA REVIDAR.

    - A PARTIDA DURARÁ 10 SEGUNDOS, TENTE 
    GANHAR O MÁXIMO NESSE PERÍODO.

    - SE VOCÊ NÃO JOGAR EM 1 SEGUNDO O 
    COMPUTADOR GANHA.
        """
        )
        self.label_regras.setStyleSheet(
            'QLabel {background: "white"; font:20px; color:"black"; border:1px solid black; border-radius:10px}'
        )
        self.label_regras.hide()

        self.start_game = QPushButton("START GAME", self)
        self.start_game.move(350, 400)
        self.start_game.resize(200, 50)
        self.start_game.setStyleSheet(
            'QPushButton {font:30px bold; color: "white"; border:2px solid white; background: "black"; border-radius:10px;} QPushButton:hover{background:"white"; color:"black"}'
        )
        self.start_game.clicked.connect(self.start_game_click)
        self.start_game.clicked.connect(self.timeout)
        self.start_game.hide()

        self.carregar_janela()

        self.placar = QLabel(self)
        self.placar.move(370, 0)
        self.placar.resize(200, 50)
        self.placar.setText("PLACAR")
        self.placar.setStyleSheet('QLabel {font:35px; color:"white"}')
        self.placar.hide()

        self.placar_player = QLabel(self)
        self.placar_player.move(250, 80)
        self.placar_player.resize(20, 50)
        self.placar_player.setText(str(self.placar_jogador))
        self.placar_player.setStyleSheet('QLabel {font:35px; color:"green"}')
        self.placar_player.hide()

        self.player_imagem = QLabel(self)
        self.player_imagem.move(290, 50)
        self.player_imagem.resize(100, 100)
        self.player_imagem.setScaledContents(True)
        self.player_imagem.setPixmap(QtGui.QPixmap("imagens_ppt/player1.png"))
        self.player_imagem.hide()

        self.vs = QLabel(self)
        self.vs.move(400, 80)
        self.vs.resize(60, 50)
        self.vs.setScaledContents(True)
        self.vs.setPixmap(QtGui.QPixmap("imagens_ppt/vs.png"))
        self.vs.hide()

        self.pc_imagem = QLabel(self)
        self.pc_imagem.move(490, 50)
        self.pc_imagem.resize(100, 100)
        self.pc_imagem.setScaledContents(True)
        self.pc_imagem.setPixmap(QtGui.QPixmap("imagens_ppt/pc1.png"))
        self.pc_imagem.hide()

        self.placar_pc = QLabel(self)
        self.placar_pc.move(630, 80)
        self.placar_pc.resize(20, 50)
        self.placar_pc.setText(str(self.placar_computador))
        self.placar_pc.setStyleSheet('QLabel {font:35px; color:"red"}')
        self.placar_pc.hide()

        self.timer_jogo = QLabel(self)
        self.timer_jogo.move(800, 0)
        self.timer_jogo.resize(100, 70)
        self.timer_jogo.setText(str(self.main_timer_10))
        self.timer_jogo.setStyleSheet('QLabel {font:70px; color:"red"}')
        self.timer_jogo.hide()
        self.qtimer_timer_jogo = QTimer()
        self.qtimer_timer_jogo.timeout.connect(self.timer1)

        self.contador = QLabel(self)
        self.contador.move(400, 200)
        self.contador.resize(200, 200)
        self.contador.setText(str(self.contador_valor))
        self.contador.setStyleSheet('QLabel {font:200px; color:"green"}')
        self.contador.hide()

        self.timer = QTimer()
        self.timer.timeout.connect(self.timeout)

        self.pedra_botao = QPushButton("Pedra",self)
        self.pedra_botao.move(180, 430)
        self.pedra_botao.resize(150, 50)
        self.pedra_botao.setStyleSheet(
            'QPushButton {font:30px bold; color: "white"; border:2px solid white; background: "black"; border-radius:10px;} QPushButton:hover{background:"white"; color:"black"}')
        self.pedra_botao.clicked.connect(lambda : self.jogada(0))
        self.pedra_imagem = QLabel(self)
        self.pedra_imagem.move(200, 320)
        self.pedra_imagem.resize(100, 100)
        self.pedra_imagem.setScaledContents(True)
        self.pedra_imagem.setPixmap(QtGui.QPixmap("imagens_ppt/pedra.png"))
        self.pedra_imagem.hide()
        self.pedra_botao.hide()

        self.papel_botao = QPushButton("Papel", self)
        self.papel_botao.move(380, 430)
        self.papel_botao.resize(150, 50)
        self.papel_botao.setStyleSheet(
            'QPushButton {font:30px bold; color: "white"; border:2px solid white; background: "black"; border-radius:10px;} QPushButton:hover{background:"white"; color:"black"}')
        self.papel_botao.clicked.connect(lambda : self.jogada(1))
        self.papel_imagem = QLabel(self)
        self.papel_imagem.move(400, 320)
        self.papel_imagem.resize(100, 100)
        self.papel_imagem.setScaledContents(True)
        self.papel_imagem.setPixmap(QtGui.QPixmap("imagens_ppt/papel.png"))
        self.papel_botao.hide()
        self.papel_imagem.hide()

        self.tesoura_botao = QPushButton("Tesoura", self)
        self.tesoura_botao.move(580, 430)
        self.tesoura_botao.resize(150, 50)
        self.tesoura_botao.setStyleSheet(
            'QPushButton {font:30px bold; color: "white"; border:2px solid white; background: "black"; border-radius:10px;} QPushButton:hover{background:"white"; color:"black"}')
        self.tesoura_botao.clicked.connect(lambda : self.jogada(2))
        self.tesoura_imagem = QLabel(self)
        self.tesoura_imagem.move(600, 320)
        self.tesoura_imagem.resize(100, 100)
        self.tesoura_imagem.setScaledContents(True)
        self.tesoura_imagem.setPixmap(QtGui.QPixmap("imagens_ppt/tesoura.png"))
        self.tesoura_botao.hide()
        self.tesoura_imagem.hide()

        self.escolha = QLabel(self)
        self.escolha.setText("ESCOLHA:")
        self.escolha.move(10, 430)
        self.escolha.resize(150, 50)
        self.escolha.setStyleSheet('QLabel {font:30px; color:"blue"}')
        self.escolha.hide()

        self.o_pc_jogou = QLabel(self)
        self.o_pc_jogou.setText("O COMPUTADOR JOGOU: ")
        self.o_pc_jogou.move(10, 190)
        self.o_pc_jogou.resize(350, 50)
        self.o_pc_jogou.setStyleSheet('QLabel {font:30px; color:"yellow"}')
        self.o_pc_jogou.hide()

        self.imagem_escolha_pc = QLabel(self)
        self.imagem_escolha_pc.move(390, 170)
        self.imagem_escolha_pc.resize(100, 100)
        self.imagem_escolha_pc.setScaledContents(True)
        self.imagem_escolha_pc.setPixmap(QtGui.QPixmap("imagens_ppt/tesoura.png"))
        self.imagem_escolha_pc.hide()

        self.lbl_resultado = QLabel(self)
        self.lbl_resultado.setText("EMPATE")
        self.lbl_resultado.move(700, 190)
        self.lbl_resultado.resize(200, 50)
        self.lbl_resultado.setStyleSheet('QLabel {font:30px; color:"yellow"}')
        self.lbl_resultado.hide()

        self.fim_jogo = QLabel(self)
        self.fim_jogo.setText("FIM DE JOGO")
        self.fim_jogo.move(250, 150)
        self.fim_jogo.resize(500, 70)
        self.fim_jogo.setStyleSheet('QLabel {font:70px; color:"RED"}')
        self.fim_jogo.hide()

        self.lbl_novamente = QLabel(self)
        self.lbl_novamente.setText("JOGAR NOVAMENTE?")
        self.lbl_novamente.move(260, 360)
        self.lbl_novamente.resize(500, 70)
        self.lbl_novamente.setStyleSheet('QLabel {font:40px; color:"white"}')
        self.lbl_novamente.hide()

        self.btn_sim = QPushButton("SIM", self)
        self.btn_sim.move(280, 430)
        self.btn_sim.resize(150, 50)
        self.btn_sim.setStyleSheet(
            'QPushButton {font:30px bold; color: "white"; border:2px solid white; background: "black"; border-radius:10px;} QPushButton:hover{background:"green"; color:"white"}'
        )
        self.btn_sim.clicked.connect(self.novamente)
        self.btn_sim.hide()

        self.btn_nao = QPushButton("NÃO", self)
        self.btn_nao.move(470, 430)
        self.btn_nao.resize(150, 50)
        self.btn_nao.setStyleSheet(
            'QPushButton {font:30px bold; color: "white"; border:2px solid white; background: "black"; border-radius:10px;} QPushButton:hover{background:"red"; color:"white"}'
        )
        self.btn_nao.clicked.connect(self.sair)
        self.btn_nao.hide()

        self.lbl_vencedor = QLabel(self)
        self.lbl_vencedor.setText("O VENCEDOR É: ")
        self.lbl_vencedor.move(250, 250)
        self.lbl_vencedor.resize(500, 70)
        self.lbl_vencedor.setStyleSheet('QLabel {font:40px; color:"blue"}')
        self.lbl_vencedor.hide()

        self.imagem_vencedor = QLabel(self)
        self.imagem_vencedor.move(550, 220)
        self.imagem_vencedor.resize(150, 150)
        self.imagem_vencedor.setScaledContents(True)
        self.imagem_vencedor.setPixmap(QtGui.QPixmap("imagens_ppt/player1.png"))
        self.imagem_vencedor.hide()


    def timeout(self):
        self.contador.setText(str(self.contador_valor))
        self.contador_valor -= 1
        if self.timer.isActive() == False and self.iniciou == False:
            self.timer.start(1000)
        if self.contador_valor < 0:
            self.iniciou = True
            self.timer.stop()
            self.contador.hide()
            self.pedra_botao.show()
            self.pedra_imagem.show()
            self.papel_botao.show()
            self.papel_imagem.show()
            self.tesoura_botao.show()
            self.tesoura_imagem.show()
            self.escolha.show()
            self.o_pc_jogou.show()
            self.sortear_jogada_pc()
            self.timer1()
            self.imagem_escolha_pc.show()


    def timer1(self):
        self.timer_jogo.setText(str(self.main_timer_10))
        self.main_timer_10 -= 1

        if self.qtimer_timer_jogo.isActive() == False and self.iniciou_main_timer == False:
            self.qtimer_timer_jogo.start(1500)
        
        if self.jogada_usuario == 'Demorou':
            if not self.primeira_vez:
                self.mostrar_resultado("DEMOROU", 'red')
                self.placar_computador += 1
                self.placar_pc.setText(str(self.placar_computador))
            else:
                self.primeira_vez = False

        elif self.jogada_computador == self.jogada_usuario:
            self.placar_empate += 1
            self.mostrar_resultado("EMPATE", 'yellow')
        else:
            
            if self.jogada_computador == "Pedra": #jogou pedra
                if self.jogada_usuario == "Papel":
                    self.mostrar_resultado("VITÓRIA", 'green')
                    self.placar_jogador += 1
                    self.placar_player.setText(str(self.placar_jogador))
                elif self.jogada_usuario == "Tesoura":
                    self.mostrar_resultado("DERROTA", 'red')
                    self.placar_computador += 1
                    self.placar_pc.setText(str(self.placar_computador))
            elif self.jogada_computador == "Papel": #jogou papel
                if self.jogada_usuario == "Pedra":
                    self.mostrar_resultado("DERROTA", 'red')
                    self.placar_computador += 1
                    self.placar_pc.setText(str(self.placar_computador))
                elif self.jogada_usuario == "Tesoura":
                    self.mostrar_resultado("VITÓRIA", 'green')
                    self.placar_jogador += 1
                    self.placar_player.setText(str(self.placar_jogador))

            elif self.jogada_computador == "Tesoura": #jogou tesoura
                if self.jogada_usuario == "Pedra":
                    self.mostrar_resultado("VITÓRIA", 'green')
                    self.placar_jogador += 1
                    self.placar_player.setText(str(self.placar_jogador))
                    
                elif self.jogada_usuario == "Papel":
                    self.mostrar_resultado("DERROTA", 'red')
                    self.placar_computador += 1
                    self.placar_pc.setText(str(self.placar_computador))

        self.jogada_usuario = 'Demorou'
        self.sortear_jogada_pc()
    
            
        if self.main_timer_10 < 0:
            self.iniciou_main_timer = True
            self.qtimer_timer_jogo.stop()
            self.imagem_escolha_pc.hide()
            self.resultado_fim_jogo()


    def mostrar_resultado(self, resultado, cor):
        self.lbl_resultado.show()
        self.lbl_resultado.setText(resultado)
        self.lbl_resultado.setStyleSheet('QLabel {font:30px; color:"' + cor +'"}')


    def resultado_fim_jogo(self):
        self.pedra_botao.hide()
        self.pedra_imagem.hide()
        self.papel_botao.hide()
        self.papel_imagem.hide()
        self.tesoura_botao.hide()
        self.tesoura_imagem.hide()
        self.escolha.hide()
        self.o_pc_jogou.hide()
        self.imagem_escolha_pc.hide()
        self.lbl_resultado.hide()
        self.fim_jogo.show()
        self.lbl_vencedor.show()
        if self.placar_computador > self.placar_jogador:
            self.imagem_vencedor.setPixmap(QtGui.QPixmap("imagens_ppt/pc1.png"))
        elif self.placar_computador < self.placar_jogador:
            self.imagem_vencedor.setPixmap(QtGui.QPixmap("imagens_ppt/player1.png"))
        elif self.placar_computador == self.placar_jogador:
            self.lbl_vencedor.setText("      EMPATE!!!")
            self.imagem_vencedor.setPixmap(QtGui.QPixmap("imagens_ppt/empate.png"))
        self.imagem_vencedor.show()
        self.lbl_novamente.show()
        self.btn_sim.show()
        self.btn_nao.show()
        

    def start_click(self):
        self.start.hide()
        self.imagem.hide()
        self.label1.show()
        self.label_regras.show()
        self.start_game.show()


    def start_game_click(self):
        self.label1.hide()
        self.label_regras.hide()
        self.start_game.hide()
        self.placar.show()
        self.placar_player.show()
        self.player_imagem.show()
        self.vs.show()
        self.timer_jogo.show()
        self.pc_imagem.show()
        self.placar_pc.show()
        self.contador.show()


    def novamente(self):
        self.close()
        iniciar()


    def carregar_janela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.setStyleSheet('background: "black"')
        self.show()
        

    def sortear_jogada_pc(self):
        self.opcoes = ("Pedra", "Papel", "Tesoura")
        computador = randint(0, 2)
        imagens = ("imagens_ppt/pedra.png", "imagens_ppt/papel.png", "imagens_ppt/tesoura.png")
        self.imagem_escolha_pc.setPixmap(QtGui.QPixmap(imagens[computador]))

        self.pedra_botao.setDisabled(False)
        self.pedra_botao.setStyleSheet(
            'QPushButton {font:30px bold; color: "white"; border:2px solid white; background: "black"; border-radius:10px;} QPushButton:hover{background:"white"; color:"black"}')

        self.papel_botao.setDisabled(False)
        self.papel_botao.setStyleSheet(
            'QPushButton {font:30px bold; color: "white"; border:2px solid white; background: "black"; border-radius:10px;} QPushButton:hover{background:"white"; color:"black"}')

        self.tesoura_botao.setDisabled(False)
        self.tesoura_botao.setStyleSheet(
            'QPushButton {font:30px bold; color: "white"; border:2px solid white; background: "black"; border-radius:10px;} QPushButton:hover{background:"white"; color:"black"}')

        self.jogada_computador = self.opcoes[computador]
        

    def jogada(self, escolha_usuario):
        self.pedra_botao.setDisabled(True)
        self.pedra_botao.setStyleSheet('QPushButton {font:30px bold; color: "white"; border:2px solid black; background: "grey"; border-radius:10px}')

        self.papel_botao.setDisabled(True)
        self.papel_botao.setStyleSheet('QPushButton {font:30px bold; color: "white"; border:2px solid black; background: "grey"; border-radius:10px}')

        self.tesoura_botao.setDisabled(True)
        self.tesoura_botao.setStyleSheet('QPushButton {font:30px bold; color: "white"; border:2px solid black; background: "grey"; border-radius:10px}')

        self.opcoes = ("Pedra", "Papel", "Tesoura")
        self.jogada_usuario = self.opcoes[escolha_usuario]
        self.resposta_jogador = self.jogada_usuario


    def sair(self):
        sys.exit(0)


if __name__ == "__main__":
    aplicacao = QApplication(sys.argv)
    iniciar()
    sys.exit(aplicacao.exec())
