galera = []
dados = []

while True:
    dados.append(str(input('NOME: ')))
    dados.append(int(input('PESO: ')))
    galera.append(dados[:])
    dados.clear()
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break

print(f'Foram cadastradas {len(galera)}')

