primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Informe a razão: '))
decimo = primeiro_termo + (10 - 1) * razão

for c in range(primeiro_termo, decimo * razão, razão):
    print('{}'.format(c), end= '->')
print('ACABOU')