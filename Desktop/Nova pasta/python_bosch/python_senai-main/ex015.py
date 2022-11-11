#Construa um programa que peça pro usuário digitar um número. Com base no valor digitado, verifique se atende a algum requisito e retorne o respectivo valor:
#● Divisível por 3 = Fizz
#● Divisível por 5 = Buzz
#● Divisível por 3 e 5 = FizzBuzz
#● Não atende nenhuma das condições acima, retorne o próprio número'''

numero = int(input('Digite um número: '))
if numero%3==0 and numero%5==0:
    print('FizzBuzz')
elif numero%3==0:
    print('Fizz')
elif numero%5==0:
    print('Buzz')
else:
    print(f'{numero} Não é divisível por 5 nem por 3.')
