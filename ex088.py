import random
numeros_sorteados = list()
jogo = list()
print('\033[33m=-=\033[m' * 15)
print('\033[1;33m------------------MEGA SENA------------------\033[m')
print('\033[33m=-=\033[m' * 15)

cont = 0
jogos = int(input('Quantos jogos voce quer sortear: '))
tot = 1


while tot <= jogos:
    while True:
        num = random.randint(0,60)
        if num not in numeros_sorteados:
            numeros_sorteados.append(num)
            cont += 1
        if cont >= 6:
            break
    numeros_sorteados.sort()
    jogo.append(numeros_sorteados[:])
    numeros_sorteados.clear()
    tot += 1
    
for i, l in enumerate(jogo):
    print(f'{i + 1}° jogo = {l}')
    






