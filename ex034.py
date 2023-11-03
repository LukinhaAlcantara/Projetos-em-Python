# perguntar o sdalario de um funcionario 
# e calcular o valor de seu aumento
# para salarios superiores que 1250 fazer o calculo com 10%
# para salarios inferiores ou igual o aumento e de 15%

salario = float(input("INforme o valor do seu salario: "))

if(salario > 1250.00):
    aumento = salario * 0.10
    salario_final = salario + aumento
    print('O seu salario com aumento agora ficou em R${:.2f}'.format(salario_final))

else:
    aumento = salario * 0.15
    salario_final = salario + aumento
    print('O seu salario com aumento agora ficou em R${:.2f}'.format(salario_final))
