print('_' * 20)
print('SEQUENCIA DE FIBONACCI')
print('_' * 20)
n = int(input('Quantos termos voce quer mostar? '))
t1 = 0
t2 = 1

cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')