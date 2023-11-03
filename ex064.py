c = 0
soma = 0
cont = 0

while c != 999:
    c = int(input('Digite um numero: '))
    if c != 999:
        if c >= 0:
            cont += 1
            soma += c



print('A soma total dos numeros foi {} e o total de digitados foram {}'.format(soma, cont))