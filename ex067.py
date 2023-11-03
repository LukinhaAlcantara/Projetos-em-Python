from time import sleep
print('-~' * 15)
print('-----------TABUADA-----------')
print('--PARA PARAR TECLE NEGATIVO--')
print('-~' * 15)
t = 0

while True:
    num = int(input('Digite um numero para ver a sua tabuada: '))
    if num < 0:
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'|{num} x {c} = ', num * c ,'|')
    print('-' * 30)
print('PROGRAMA ENCERRADO!! Volte sempre')

