valores = []
cont = 0
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? [S/N] '))
    cont += 1
    if resp in 'Nn':
        break

valores.sort(reverse=True)

print(f'Voce digitou {cont} elementos')
print(f'Os valores digitados foram {valores}')

if 5 in valores:
    print(f'O valor 5 esta dentro da lista')
else:
    print(f'O valor 5 nao foi encontrado na lista')