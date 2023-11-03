from random import randint

numeros = list()


def sorteio():
    for c in range(0, 5):
        num_sorteados = (randint(0, 100))
        numeros.append(num_sorteados)
    print(numeros)
    
def somaPar():
    for c in enumerate(numeros):
        if c % 2 == 0:
            somapar += c
            contpar += 1
    print(f'A soma dos valores par foi de {somapar} e foram {contpar} numeros somados')
    
sorteio()
somaPar()