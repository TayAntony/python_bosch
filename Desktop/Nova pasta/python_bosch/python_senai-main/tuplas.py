#tuplas são imutaveis, será do mesmo jeito que digitada no começo ate o final do programa, sem alterar, trocar ou adicionar valores
#set é um tipo (lista, dicionario, tupla)

numeros = [22, 51, 44, 15]
primeiro = set(numeros) #convertendo uma lista em set
segundo = {1, 32, 44} #criando um set direto usando {}
lista = list(segundo) #convertendo set em lista
lista2 = tuple(lista) #convertendo lista em tupla

print(primeiro | segundo) #obter todos o snúmeros sem repetição e junta as listas
print(primeiro & segundo) #trazer os números em comum nos dois sets
print(primeiro - segundo) #trazer o primeiro excluindo os valores em comum
print(primeiro ^ segundo) #trazer os elementos que não se repetem
