n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1+n2
subtracao = n1-n2
divisao = n1/n2
multiplicacao = n1*n2
potencia = n1**n2
div_int = n1//n2
resto_div = n1%n2

print(f'''Um valor: {n1}
Outro valor: {n2}
A soma vale: {soma}
A subtração vale: {subtracao}
A multiplicação vale: {multiplicacao}
A divisão vale: {divisao:.2f}
A divisão inteira vale: {div_int}
A potenciação vale: {potencia}
O resto da divisão vale: {resto_div}
''')