# inicializando variaveis
num = 0
media = 0
maior = 0
menor = 0
soma = 0
cont = 0

# instruçoes 
print('____________________________')
print('    PARA PARAR TECLE 999    ')
print('----------------------------')

# enquanto
while num != 999:
    num = int(input('Digite um numero: '))
    if num != 999:
        # soma e contagem dos numeros
        if num >= 0:
            soma += num
            cont += 1
        # media
        media = soma / cont
        # maior e menor
        if num >= 0:
            maior = num
            menor = num
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num
# verificar se quer continuar
num = int(input('DESEJA CONTINUAR?\n[1]SIM\n[999]NÂO\nRESPOSTA: '))

print('A media entre eles será {:.2f}'.format(media))
print('O maior valor vai ser o {}'.format(maior))
print('O menor valor vai ser o {}'.format(menor))