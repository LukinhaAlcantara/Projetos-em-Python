# programa deve calcular o valor de um produto
# olhando seu preço normal e forma de pagamento
# a vista dinheiro ou cheque tera 10% de desconto
# a vista no cartao tem 5% de desconto
# em ate 2x no cartao permanece o preço normal 
# 3 vezes ou mais tera acrescimos de juros de 20%

valor_inicial = float(input("DIgite o valor do produto: "))
escolha = str(input('Qual a forma de pagamento dinheiro, cheque, debito ou credito1x, credito2x ou creditomais:'))

if(escolha == 'dinheiro' and escolha == 'cheque'):
    valor_final = valor_inicial - (valor_inicial * 0.10)
    print('O total a pagar será R${:.2f}'.format(valor_final))
    
elif(escolha == 'debito'):
    valor_final = valor_inicial - (valor_inicial * 0.05)
    print('O valor total será de R${:.2f}'.format(valor_final))
    
elif(escolha ==  'credito1x' and escolha == 'credito2x'):
    print('O valor será R${:.2f}'.format(valor_inicial))
    
else:
    valor_final = valor_inicial + (valor_inicial * 0.20)
    print('O valor total será R${}'.format(valor_final))