
lista = [3, 5, 6, 1, 20, 7]
letras = ['a', 'b', 'c', 'd', 'e']
letras.append('f') #adiciona um elemendo no último lugar da lista
letras.insert(0, 'aa') # adiciona um elemento no indice escolhido
letras.pop() # remove o ultimo elemento da lista
letras.remove('b') # remove o elemento pelo valor escolhido
del letras [2] # del remove um elemento pelo índice escolhido, também pode ser escrito com [2:3], [2:]
lista.sort() # ordena os valores da lista em ordem crescente
lista.sort(reverse=True) # ordena em ordem decrescente
primeiro, *resto, ultimo= lista #extrair dados de uma lista
print(primeiro)
print(resto)
print(ultimo)

lista1 = [2, 4, 5]
lista2 = lista1 #uma ligação de listas (ocupam o mesmo espaço na memória)

lista2 = lista1[:] # uma cópia da lista 1
lista2[1] = 5 # altera um valor pelo índice


#colocando uma lista dentro de outra lista
lista3 = ['a', 'b']
lista4 = ['c', 'd']
juntar = list()
juntar.append(lista1)
juntar.append(lista2)
print(juntar)