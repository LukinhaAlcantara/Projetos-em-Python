# escreva um codigo que a maquina escolha um numero de 0 a 5
# depois deixe o usuario tentar a divinha-lo

import random as rd

num_aleatorio = rd.randint(0, 5)

num_usuario = int(input("Tente adivinhar o numero sorteado pelo computador: "))

if(num_usuario == num_aleatorio):
    print("Parabéns você acertou o numero {}".format(num_aleatorio))

else:
    print("Tente Novamente você erreou o numero {}".format(num_aleatorio))