# ler o ano de nascimento de um joven
# e informe de acordo com sua idade :
# se ele ainda vai se alistar ao serviço militar 
# se esta na hora dele se alistar
# ou se ja passou da hora dele se alistar
# e mostar tambem o tempo que falta ou passou 

ano = int(input("Digite o seu ano de anscimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade = ano_atual - ano

if(idade == 18):
    print('\033[4;32mEsta na hora de você se alistar\033[m')
    
elif(idade < 18):
    tempo_que_falta = 18 - idade
    print('\033[4;36mVocê ainda nao precisa se alistar\033[m')
    print('\033[4;36mAinda faltam {} anos.'.format(tempo_que_falta))
    
else:
    tempo_que_falta = idade - 18
    print('\033[4;31mJá passou da hora de se alistar')
    print('\033[4;31mJá se passou {} anos para você se alistar'.format(tempo_que_falta))
    
    