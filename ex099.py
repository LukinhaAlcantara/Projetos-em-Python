def maior():
    num_digitados = int(input('Quantos numeros serao inseridos: '))
    for c in range(0, num_digitados):
        num = int(input('Digite um numero: '))
        if c == 0:
            maior = num
            menor = num
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num
    print(f'O maior valor foi o {maior}')
    print(f'O menor valor foi o {menor}')


maior()