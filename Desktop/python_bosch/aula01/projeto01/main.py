import temporizador

def laco_infinito():
    contador = 0
    while True:
        if contador % 5 == 0:
            continue
        print(contador)
        contador += 1
        if contador >50:
            break

if __name__ == '__main__':
    print('Estou contando')
    laco_infinito()
    temporizador.contadores()