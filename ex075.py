num = (int(input('Digite um nuemro: ')),
    int(input('Digite um nuemro: ')),
    int(input('Digite um nuemro: ')),
    int(input('Digite um nuemro: ')))

print(f'Você digitou os valores {num}')
print(f'O numero 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O numero 3 apareceu na {num.index(3)}ª posiçao')
else:
    print('O valor 3 nao foi digitado!!')
print(f'Os valores digitados pares foram', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')