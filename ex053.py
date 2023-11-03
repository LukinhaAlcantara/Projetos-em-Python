frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
tudo_junto = ''.join(palavras)
inverso = ''
for letra in range(len(tudo_junto) - 1, -1, -1):
    inverso += tudo_junto[letra]
print("O iverso de {} é {}".format(tudo_junto, inverso))
if inverso == tudo_junto:
    print('A frase digitada e um palimetro')
else:
    print("A frase digitada nao é um palimetro")