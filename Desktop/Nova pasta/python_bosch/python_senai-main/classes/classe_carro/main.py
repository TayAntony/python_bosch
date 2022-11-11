import inquirer
marca_opcoes = [
	inquirer.List(
		'escolha',
		message='MARCA DO CARRO',
		choices=('Toyota', 'Chevrolet', 'Ford', 'Fiat', 'Volkswagen')
	)
]
marca = inquirer.prompt(marca_opcoes)['escolha']

marcas_modelos_correspondentes = {
	'Toyota': ('Corolla', 'RAV4', 'Hilux', 'Camry', 'Prius'),
	'Chevrolet': ('Camaro', 'Cruze', 'Onix', 'Tracker', 'Spin'),
	'Ford': ('Ka', 'Ranger', 'Fiesta', 'Ecosport', 'Edge'),
	'Fiat': ('Mobi', 'Argo', 'Pulse', 'Cronos', 'Fiorino'),
	'Volkswagen': ('Polo', 'Jeta', 'Gol', 'Voyage', 'Fox')
}

opcoes_modelo = [
	inquirer.List(
		'escolha',
		message='ESCOLHA O MODELO',
		choices=marcas_modelos_correspondentes[marca]
	)
]

modelo_escolhido = inquirer.prompt(opcoes_modelo)['escolha']

placa = input('Digite a placa do carro: ').upper()

opcoes_carro = [
	inquirer.List(
		'consumo',
		message='CONSUMO DO CARRO (km/L)',
		choices=('8km/L', '10km/L', '13km/L', '15km/L', '18km/L', '20km/L', '22km/L', '25km/L')
	),
	inquirer.List(
		'tanque',
		message='NÍVEL DO TANQUE',
		choices=('Baixo', 'Médio', 'Alto', 'Reserva')
	),
	inquirer.List(
		'categoria',
		message='CATEGORIA DO CARRO',
		choices=('Hatch', 'Sedan', 'SUV', 'Pick-up')
	),
	inquirer.List(
		'airbag',
		message='QUANTIDADE DE AIRBAGS',
		choices=(1, 2, 3, 4)
	),
	inquirer.List(
		'porta_mala',
		message='QUANTIDADE DE LITROS NO PORTA MALA',
		choices=(150, 200, 250, 300, 400, 500, 700)
	),
	inquirer.List(
		'conversivel',
		message='CONVERSÍVEL?',
		choices=('SIM', 'NÃO')
	)
]

escolhas_carro = inquirer.prompt(opcoes_carro)


