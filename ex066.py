print('-=' * 20)
print('CASO QUISER PARAR TECLE 999')
print('-=' * 20)

cont = 0
s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
    cont +=1

print(f'A soma entre eles é {s} e o numero de digitados foi {cont}')