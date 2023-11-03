import random as rd

perg = 'S'
cont_erros = 0

print('\033[33m-=\033[m' * 27)
print('\033[33m------------\033[m\033[31mTENTE VENCER O SEU COMPUTADOR\033[m\033[33m------------\033[m')
print('\033[33m-=\033[m' * 27)
while perg == 'S':
    num_aleatorio = rd.randint(0, 10)
    num_usuario = int(input("Tente adivinhar o numero sorteado pelo computador entre 0 e 10: "))
    if(num_usuario == num_aleatorio):
        print("Parabéns você acertou o numero {}".format(num_aleatorio))
        perg = 'N'
    else:
        print("Tente Novamente você erreou o numero {}".format(num_aleatorio))
        cont_erros += 1

print('\033[4;31mVocê precisou de {} tentativas para vencer o computador\033[m'.format(cont_erros).upper())
