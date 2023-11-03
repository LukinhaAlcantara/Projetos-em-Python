# ler dois numeros inteiros
# comparar esses dois numeros
# mostrando na tela um desses: 
# o primeiro e maior
# o segundo e maior
# nao tem maior eles sao iguais

num1 = int(input("DIgite um numero: "))
num2 = int(input("Digite outro numero: "))

maior = num1

if(maior > num2):
    print('\033[4;36mO primeiro é o maior\033[m')
    
elif(maior < num2):
    print('\033[4;35mO segundo é o maior\033[m')
    
else:
    print('\033[4;33mNao ha valor maior os dois sao iguais!!\033[m')