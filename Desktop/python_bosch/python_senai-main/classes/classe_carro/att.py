from carro import Ia, Menu

class Exibir:
    def atualizar(self):
        contador = 0
        while True:
            print(f'A distância atual é: {Ia.distancia}')
            Ia.distancia -= Ia.velocidade
            contador += 1
            if Ia.distancia <= 0:
                print('Você chegou ao seu destino!')
                break