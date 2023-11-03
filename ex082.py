lista = []
par = []
impar = []

while True:
    n = int(input('Digite umm valor: '))
    if n % 2 == 0:
        lista.append(n)
        par.append(n)
    elif n % 2 == 1:
        lista.append(n)
        impar.append(n)
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break

lista.sort()
par.sort()
impar.sort()

print(f'Voce digitou os valores {lista}')
print(f'Os valores pares foram {par}')
print(f'Os valores impares foram {impar}')
