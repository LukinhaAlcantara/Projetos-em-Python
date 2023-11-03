from random import choices

n1 = str(input('primeiro aluno: '))
n2 = str(input('segundo aluno: '))
n3 = str(input('terceiro aluno: '))
n4 = str(input('quarto aluno: '))

lista = [n1, n2, n3, n4]

escolhido = choices(lista)

cores = {
    'limpa' : '\033[m' ,
    'azul' : '\033[34m' ,
    'amarelo' : '\033[33m' , 
    'pretoebranco' : '\033[7;30m'
    }

print('o aluno escolhido foi {}{}{}'.format(cores['amarelo'] escolhido, cores['limpa']))