import datetime
def main():
    nascimento = input('Digite sua data de  nascimento (dd/mm/aaaa): ').split('/')
    #pegando o dia, mês e ano do computador
    dia_atual = datetime.date.today().day
    mes_atual = datetime.date.today().month
    ano_atual = datetime.date.today().year

    #convertendo as strings da lista nascimento em numeros
    nascimento_dia = int(nascimento[0])
    nascimento_mes = int(nascimento[1])
    nascimento_ano = int(nascimento[2])

    #calculando a idade exata 
    ano_idade = ano_atual - nascimento_ano
    mes_idade = mes_atual - nascimento_mes
    dia_idade = dia_atual - nascimento_dia

    print('=-'*20)
    if ano_idade >= 18 and mes_idade >= 0 and dia_idade >=0:
        if mes_idade <0:
            ano_idade -= 1
        print(f'Você tem {ano_idade} anos, {mes_idade} meses e {dia_idade} dias e pode tirar cnh')
    else:
        print(f'Você tem {ano_idade} anos, {mes_idade} meses e {dia_idade} dias e não pode tirar cnh')

if __name__ == '__main__':
    main()
