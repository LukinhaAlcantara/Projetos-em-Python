# iniciando variaveis
soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = 0
totmulher20 = 0

# Estruturas de for
for p in range(1, 5):
    # Entrada de dados
    print('----{}ª PESSOA ----'.format(p))
    nome = str(input('NOME: ')).strip()
    idade = int(input("IDADE: "))
    sexo = str(input('SEXO[M/F]: ')).strip()
    soma_idade += idade
    
    # conferindo qual e o nome do homem mais velho
    if p == 1 and sexo in 'Mm' :
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem :
        maior_idade_homem = idade
        nome_velho = nome
    
    # conferindo quantas mulheres tem menos de 20 anos
    if sexo in 'Ff' and idade < 20 :
        totmulher20 += 1

# saida de dados
media_idade = soma_idade / 4
print('A media de idade do grupo é de {} anos.'.format(media_idade))
print('O homem mais velho tem {} e se chama {}'.format(maior_idade_homem, nome_velho))
print('O total de mulheres com menos de 20 de anons é {}'.format(totmulher20))