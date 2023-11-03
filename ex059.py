from time import sleep

maior = 0
c = 0

num_1 = float(input('Digite o primeiro valor: '))
num_2 = float(input('Digite o segundo valor: '))

while c != 5:
    # tempo 
    sleep(1)
    # opçao de escolha
    print('-=' * 11)
    print('-------ESCOLHA-------')
    escolha = int(input('[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS NUMEROS\n[5]SAIR DO PROGRAMA\n'))
    print('-=' * 11)
    # soma
    if escolha == 1:
        soma = num_1 + num_2
        print('A soma dos numeros resultou em {:.2f}'.format(soma))
    # multiplicação
    elif escolha == 2:
        mult = num_1 * num_2
        print('O produto dos dois numeros resultou em {:.2f}'.format(mult))
    # maior
    elif escolha == 3:
        maior = num_1
        if maior > num_2:
            print('O maior numero entre {:.2f} e {:.2f} é o primeiro numero!!'.format(maior, num_2))
        else:
            print('O maior numero entre {:.2f} e {:.2f} é o segundo numero'.format(num_2, maior))
    # novos numeros
    if escolha == 4:
        num_1 = float(input('Digite o primeiro valor: '))
        num_2 = float(input('Digite o segundo valor: '))
    # sair do programa
    if escolha == 5:
        c = 5 

print('________FIM_______')