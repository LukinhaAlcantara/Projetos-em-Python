primeiro = int(input('PRIMEIRO TERMO: '))
razao = int(input('RAZÂO: '))
termo = primeiro
cont = 1
while cont <=10:
    print('{} -> '.format(termo),end='')
    termo += razao
    cont +=1
print("FIM")
