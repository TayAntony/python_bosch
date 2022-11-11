cidade = str(input('Digite o nome de uma cidade: ')).strip() #pedindo o nome da cidade e tirando os espaços
encontre = cidade.find('SANTO') #usando find para encontrar santo 
print(cidade[0:5].upper() == 'SANTO') #colocando santo em maiusculas para o programa identificar se foi escrito nos primeiros 5 indices/letras

#retorna true ou false se começar com santo ou não