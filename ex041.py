# ler um ano de nascimento de um atleta
# e mostre a sua categoria
# ate 9 anos e mirim
# ate 14 anos e infantil
# ate 19 anos e junior
# ate 20 anos e senior
# acima de 20 e master

ano = int(input("Digite o ano de seu nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade = ano_atual - ano

if(idade <= 9):
    print('\033[4;30mMirim\033[m')

elif(idade <= 14):
    print('\033[4;31mInfantil\033[m')
    
elif(idade <= 19):
    print('\033[4;32mJunior\033[m')
    
elif(idade == 20):
    print('\033[4;33mSênior\033[m')
    
else:
    print('\033[4;34mMaster\033[m')