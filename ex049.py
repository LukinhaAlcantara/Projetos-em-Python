num = int(input('Escolha um numero para ver a sua tabuada: '))
print('\033[1; 33m-=\033[m' * 7)
print('\033[1; 34m<--TABUADA-->\033[m')
print('\033[1; 33m-=\033[m' * 7)
for c in range(0, 11):
    print(c ,'X', num, '=', c * num )