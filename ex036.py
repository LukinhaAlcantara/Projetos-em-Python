# programa para aprovar emprestimo bancario
# tera que perguntar:
# valor da casa
# valor do salario
# quantos anos eles querem pagar 
# calcular a pestação mensal
# e que nao pode exceder 30% do salario
# ou entao o emprestimo sera negado

valor_casa = float(input("Qual o valor da casa: "))
valor_salario = float(input("Qual o valor do salario do comprador: "))
anos = float(input("Por quantos anos pretendem pagar a casa:")) 

mensal = anos * 12
valor_mensal = valor_casa / mensal

porcentagem = valor_salario * 0.30

if(valor_mensal < porcentagem):
    print('\033[4;32mO emprestimo será concedido\033[m')
    
else:
    print('\033[4;31mEmprestimo negado\033[m')