# deve ler a velociade de um carro
# se a velociadee for acima de 80km/h
# ele deve ser multado
# e deve-se adicionar 7 reais a cada km ecedido

limite = 80

velocidade = int(input('Qual a velocidade que vc passou no radar: '))

if(velocidade > limite):
    ecedido = velocidade - limite
    valor_a_mais = ecedido * 7 + 150
    print("Voce ultrapassou a velocidade permitida na via. O valor da multa sera {}".format(valor_a_mais))
    
else:
    print("\033[34mTudo certo voce esta dentro da velocidade limite\033[m")