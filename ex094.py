result = list()
dados = dict()
list_mulh = list()
list_acim = list()

cont = 0
idade = 0

while True:
    dados['Nome'] = str(input("NOME: "))
    dados['Sexo'] = str(input('SEXO: ')).upper()
    if dados['Sexo'] not in 'MF':
        print("ERROR!! Digite a sexo novamente!!")
        dados['Sexo'] = str(input("SEXO: ")).upper()
    dados['Idade'] = int(input("IDADE: "))
    result.append(dados.copy())
    cont += 1
    idade += dados['Idade']
    if dados['Sexo'] == 'F':
        list_mulh.append(dados['Nome'])
    resp = str(input('DESEJA CONTINUAR? [S/N]: ')).upper()
    if resp == 'N':
        break

media = idade / cont

for c in range(result):
    if dados[idade] > media:
        list_acim.append(dados['Nome'])
            
print('=-' * 30)
print(f'A) Foram cadastradas {cont} pessoas!!')
print(f'B) A media de idade das pessoas cadastradas è {media:.2f}')
print(f'C) As mulheres cadastradas foram {list_mulh}')
print(f'D) As pessoas com idade acima da media são {list_acim}')
print('=-' * 30)