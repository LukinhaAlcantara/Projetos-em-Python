# ler idade e sexo de varias pessoas
# a cada pessoa cadrastada perguntar se quer continuar
# depois mostrar qunatas pessoas tem mais de 18 anos 
# quantos homens foram cadrastados
# quantas mulheres foram cadastradas que tem menos de 20 anos

cont_idade = 0
cont_masc = 0
cont_fem = 0

while True:
    print('\033[1m-\033[m' * 20)
    idade = int(input('Qual a sua idade: '))
    sexo = str(input('Qual seu sexo [M/F] ')).upper()
    if sexo != 'M' and sexo != 'F':
        sexo = str(input('Qual seu sexo [M/F] ')).upper()
    escolha = str(input('Deseja continuar [S/N] ')).upper()
    print('\033[1m-\033[m' * 20)
    if escolha == 'N':
        break
    if idade > 18:
        cont_idade += 1
    if sexo == 'M':
        cont_masc += 1
    if sexo == 'F' and idade < 20:
        cont_fem += 1

print(f'Tem {cont_idade} pessoas com mais de 18 anos')
print(f'Foram cadastrados {cont_masc} homens')
print(f'Tem {cont_fem} mulheres com menos de 20 anos cadastradas')