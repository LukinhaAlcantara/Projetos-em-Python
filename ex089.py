ficha = []

while True:  
    nome = str(input("NOME: "))
    nota_1 = int(input("NOTA1: "))
    nota_2 = int(input("NOTA2: "))
    media = (nota_1 + nota_2) / 2
    ficha.append([nome, [nota_1,nota_2], media])
    resp = str(input('Deseja continuar [S/N] '))
    if resp in 'Nn':
        break

print('-=' * 30)
print(f'{"NO.":<4} {"NOME":<10} {"MEDIA":>8}')
print("-=" * 30)

for i, a in enumerate(ficha):
    print(f'{i:<4} {a[0]:<10} {a[2]:>8}')
    
while True:
    print('-' * 36)
    opc = int(input('Deseja ver notas de qual aluno? [999 INTERROMPE]'))
    if opc == 999:
        break
        print('VOLTE SEMPRE')
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc[1]]}')
        print('<<<<<<< Volte sempre')
