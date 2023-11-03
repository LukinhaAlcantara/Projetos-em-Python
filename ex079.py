valores = []

while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('O valor ja existe na lista logo ele nao sera adicionado...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
    
valores.sort()
print(f'Voce digitou os valores {valores}')
