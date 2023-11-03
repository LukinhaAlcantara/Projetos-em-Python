# ler o peso e a altura de uma pessoa
# calcular seu IMC e mostrar seu status
# abaixo de 18.5 abaixo do peso
# entre 18.5 e 25 peso ideal
# 25 a 30 sobrepeso
# 30 a 40 obesidade
# acima de 40 obesidade morbida

altura = float(input("DIgite a sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / (altura * altura)

if(imc < 18.5):
    print('\033[4;30mAbaixo do peso\033[m')
    
elif(imc >= 18.5 and imc < 25):
    print('\033[4;31mPeso ideal\033[m')
    
elif(imc >= 25 and imc < 30):
    print('\033[4;32mSobrepeso\033[m')
    
elif(imc >= 30 and imc < 40):
    print('\033[4;33mObesidade\033[m')
    
else:
    print('\033[4;34mObesidade morbida\033[m')
    