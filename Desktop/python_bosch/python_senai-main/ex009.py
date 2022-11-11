texto = input('Digite seu nome: ')


# para colocar um replace ou find dentro de um print com um texto, é preciso usar aspas simples no print  e aspas duplas na função, ou vice versa
print(len(texto)) # lenght tamanho do nome
print(texto.strip()) # tira os espaços da direita e esquerda, ou direita/right (rstrip) ou esquerda/left (lstrip)
print(texto.count('a')) #conta quantos caracteres tem
print(texto.replace('a', '4')) # substitui todos os caracteres por outro (nesse caso substitui a por 4)
print(texto.find('a')) # encontra o índice do primeiro caractere, ou retorna -1 caso não ache
# print(texto).upper().lower()  tudo maiúsculo ou minusculo, nao recebe argumentos
# print(texto).capitalize().title()  capitalize deixa a primiera letra da frase maiúscula, e title deixa a primeira letra de cada palavra maiuscula
print(texto.split(',')) #split separa palavras por um determinado caractere, por padrão o split separa por espaço, mas dá para escolher o caractere (nesse caso a vírgula)
print('-'.join(texto)) #join coloca algum caractere entre as letras de uma frase (nesse caso o -)