def main ():
    idade = int(input('ENTRE COM SUA IDADE: '))
    #tipo_idade = type(idade)
    #print(tipo_idade)
    if idade >= 18:
        print('Você é maior de idade!')
    elif idade > 0:
        print('Você é menor de idade')
    else:
        print('Você não existe ainda')
    

if __name__ == '__main__':
    main()


