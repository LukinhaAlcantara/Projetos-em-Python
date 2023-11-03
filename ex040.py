# ler duas notas de alunos
# fazer a media 
# e se for abaixo de 5.0 e reprovado
# se for entre 5.0 e 6.9 e recuperação
# se for maior que 7.0 e aprovado

nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if(media < 5.0):
    print('\033[4;31mReprovado\033[m')
    
elif(media > 5.0 and media <= 6.9):
    print('\033[4;33mRecuperação\033[m')
    
else:
    print('\033[4;32mAprovado\033[m')
    
