# escolha de numero e par ou impar do usuario
# escolha de numero aleatorio do computador 
# fazer ifs para ver o vencedor
# fazer um while true para contionuar ate o usuario perder


from random import randint

c = 0

print('\033[1;33m-\033[m' * 35)
print('\033[1;36m___________PAR OU IMPAR___________\033[m')
print('\033[1;33m-\033[m' * 35)

cont_venc = 0

while True:
    escolha = str(input('PAR OU IMPAR [P/I] ')).upper()
    num = int(input('Escolha um numero: '))
    num_aleatorio = randint(0, 10)
    soma = num_aleatorio + num
    resultado = 'PAR' if soma % 2 == 0 else 'IMPAR'
    print(f'O numero {num} somado ao {num_aleatorio} e igual á {soma} que por sua vez é {resultado}')
    if escolha == 'P' and resultado == 'PAR':
        print('PARABENS VOCÊ VENCEU!!!!')
        print('Vamos de novo...')
        cont_venc += 1
    elif escolha == 'P' and resultado == 'IMPAR':
        print('VOCÊ PERDEU!!')
        break
    elif escolha == 'I' and resultado == 'IMPAR':
        print('VOCÊ VENCEU!!!')
        print('Vamos de novo...')
        cont_venc += 1
    else:
        print('Você perdeu!!')
        break

print(f'Você vecnceu {cont_venc} vezes')
