def voto(ano_de_nasc):
    global idade
    idade = 2023 - ano_de_nasc
    return idade


ano = voto(int(input('Qual seu ano de nascimento: ')))

if ano <= 15:
    print("Votação negada")
elif ano <=17:
    print('Votação opcional')
elif ano >= 18:
    print('Votação obrigatoria')