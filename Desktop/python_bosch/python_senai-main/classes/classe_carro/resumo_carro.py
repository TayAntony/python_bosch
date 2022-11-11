class Resumo():
    def __init__(self, marca,modelo,placa,consumo,nivelCombustivel,categoria,airbags,litrosPortaMala,conversivel):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.consumo = consumo
        self.nivelCombustivel = nivelCombustivel
        self.categoria = categoria
        self.airbags = airbags
        self.litrosPortaMala = litrosPortaMala 
        self.conversivel = conversivel

    def resumo_carro(self):
        print(f'''
\033[1;34mMarca:\033[0;0m \033[1;32m{self.marca}\033[0;0m
\033[1;34mModelo:\033[0;0m \033[1;32m{self.modelo}\033[0;0m
\033[1;34mPlaca:\033[0;0m \033[1;32m{self.placa}\033[0;0m
\033[1;34mConsumo (km/L):\033[0;0m \033[1;32m{self.consumo}\033[0;0m
\033[1;34mTanque:\033[0;0m \033[1;32m{self.nivelCombustivel}\033[0;0m
\033[1;34mCategoria:\033[0;0m \033[1;32m{self.categoria}\033[0;0m
\033[1;34mQuantidade Airbags:\033[0;0m \033[1;32m{self.airbags}\033[0;0m
\033[1;34mLitros do porta-mala:\033[0;0m \033[1;32m{self.litrosPortaMala}\033[0;0m
\033[1;34mConversível?\033[0;0m \033[1;32m{self.conversivel}\033[0;0m
''')
