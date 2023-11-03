# ler nome e preço de varios produtos
# deve perguntar após se o usuario quer continuar
# e no final mostar qual e o total gasto
# quantos produtos custam mais de R$1000
# Qual o nome do produto mais barato

soma_total = 0
cont_preço = 0
maior = 0
menor = 0 
nome_mais_barato = 0
cont = 0

print('=-' * 15)
while True:
    produto = str(input('Qual o nome do produto: '))
    preço = int(input('Qual o preço do produto: '))
    escolha = str(input('Deseja continaur? [S/N] ')).upper()
    print('=-' * 15)
    cont += 1
    soma_total += preço
    if preço > 1000:
        cont_preço += 1
    if cont == 1 or preço < menor:
        menor = preço
        nome_mais_barato = produto
    if escolha == 'N':
        break

print(f'O total gasto foi de R${soma_total}')
print(f'Foram {cont_preço} produtos que castavam mais de R$1000')
print(f'O nome do produto mais barato é {nome_mais_barato} que custa {menor:.2f}')