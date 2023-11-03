# perguntar um ano qualquer
# mostrar se esse ano e bissexto ou nao

from calendar import isleap

ano = int(input('Digite o ano: '))

if isleap(ano):
    print('É bissexto')
else:
    print('Não é bissexto')