# crie um programa que leia o nome, ano de nascimento e carteira de trabalho e idade 
# cadastrar em um dicionario
# caso o CTPS for diferente de zero o dicionario tambem recebera
# ano de contratação e salario
# calcule e acrescente alem da idade com quantos anos a pessoa vai ter que aposentar

cadastro = dict()

print('-=' * 20)
print('-----------APOSENTADORIA-----------')
print('-=' * 20)
print()
print('<=---CADASTRO---=>')


cadastro['nome'] = str(input('NOME: '))
cadastro['ano_nasc'] = int(input('ANO DE NASCIMENTO: '))
cadastro['carteira_de_trabalho'] = int(input('CARTEIRA DE TRABALHO (0 CASO NAO TIVER): '))
if cadastro['carteira_de_trabalho'] != 0:
    cadastro['ano_contra'] = int(input('ANO DE CONTRATAÇÂO: '))
    cadastro['salario'] = int(input('SALARIO: '))
    

print()
print('--------DADOS--------')
print(f'Seu nome é {cadastro["nome"]}')
print(f'Voce nasceu no ano de {cadastro["ano_nasc"]}')
print(f'Entao sua idade é {2023 - cadastro["ano_nasc"]}')
print(f'O seu salario é de R${cadastro["salario"]}')
print(f'O ano da sua aposentadoria sera em {cadastro["ano_contra"] + 35}')
