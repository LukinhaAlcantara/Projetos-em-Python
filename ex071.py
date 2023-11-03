# fazer um caixa eletronico
# com cedulas de 50 20 10 1 
# e mostrar quantas de cada cedulas vao ser necessarias
print('\033[1;31m=\033[m' * 30)
print('\033[33m          BANCO ALTRA          \033[m')
print('\033[1;31m=\033[m' * 30)

dinheiro = int(input('Qual o valor que você quer sacar? R$ '))

cont_50 = 0
cont_20 = 0
cont_10 = 0
cont_1 = 0

while True:
    if dinheiro == 0:
        break
    if dinheiro >= 50:
        dinheiro -= 50
        cont_50 += 1
    elif dinheiro >= 20:
        dinheiro -= 20
        cont_20 += 1
    elif dinheiro >= 10:
        dinheiro -= 10
        cont_10 += 1
    else:
        dinheiro -= 1
        cont_1

print(f'Total de {cont_50} cedulas de R$50')
print(f'Total de {cont_20} cedulas de R$20')
print(f'Total de {cont_10} cedulas de R$10')
print(f'Total de {cont_1} cedulas de R$1')

print('\033[1;31m=\033[m' * 30)
print('Obrigado pela preferencia volte sempre!!')

