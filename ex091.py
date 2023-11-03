# crie um programa aonde 4 jogaram o dado que tenha resultados aleatorios
# no final coloque o dicionario em ordem
# sabendo que o vencedor tirou o maior numero do dado

from random import randint

dados = dict()
resultados = list()

for c in range(1, 5):
    dados['Nome'] = str(input(f'{c}° jogador:'))
    dados['Num_aleatorio'] = randint(0, 6)
    resultados.append(dados.copy())

resultados.sort()
print(resultados)
    