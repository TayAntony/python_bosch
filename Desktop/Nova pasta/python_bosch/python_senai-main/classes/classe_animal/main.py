from classes import Animal


#passando parâmetros
animal1 = Animal('Ted', 'roedor', 1.1)
animal1.cacar() #printando a função

meu_animal = Animal() #instânciando (criar um objeto da classe)

#atribuindo valor aos objetos
nome_animal = input('Digite o nome do seu pet: ')
especie_animal = input('Digite a espécie do seu pet: ')
peso_animal = input('Digite o peso do seu pet: ')
# meu_animal.nome = nome_animal
# meu_animal.especie = especie_animal
# meu_animal.peso = peso_animal

animal3= Animal(nome=nome_animal, 
                especie=especie_animal, 
                peso=peso_animal)

animal3.sexo()
print(animal3.genero)