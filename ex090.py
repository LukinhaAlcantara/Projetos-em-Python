# faça um programa que peça nome e media de um aluno
# e guardando a situação em um dicionario
# no final mostar o conteudo na tela

dados = dict()
alunos = list()

while True:
    dados['nome'] = str(input('Nome: '))
    dados['media'] = float(input('Media: '))
    if dados['media'] <= 3:
        dados['situação'] = 'Reprovado'
    elif dados['media'] < 7:
        dados['situação'] = 'Recuperação'
    elif dados['media'] >= 7:
        dados['situação'] = 'Aprovado'
    alunos.append(dados.copy())
    resp = str(input('Deseja continuar [S/N]: ')).upper()
    if resp == 'N':
        break


for e in alunos:
    print('-=' * 40)
    for k, v in e.items():
        print(f'{k:<4} = {v:<8}', end=' ')
    print()