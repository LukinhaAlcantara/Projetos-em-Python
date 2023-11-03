# crie um programa que gerencie o aproveitamento de um jogador de futebol
# vai ler nome do jogador, quantas partidas ele jogou
# quantidade de gols feito em cada partida
# e mostre a media de gols por partida

dados_inc = dict()
dados_fnl = list()
soma = 0

nome = str(input('Qual o nome do jogador: '))
quant_part = int(input('Quantas partidas ele jogou: '))

for c in range(1, quant_part + 1):
    dados_inc['num_de_gol'] = gols = int(input(f'Quantos gols no {c}° jogo: '))
    dados_fnl.append(dados_inc.copy())
    soma = soma + gols
    
media = soma/quant_part
print('-=' * 30)
for p,n in enumerate(dados_fnl):
    print(f'Na {p}° patida foram {n[1]} gols')
print(f"Sua media de gols foi de {media:.2f} por partida")
