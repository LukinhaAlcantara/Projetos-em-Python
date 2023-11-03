valores = []
for c in range(0, 5):
    valores.append(int(input("Digite um valor: ")))

print(f'O maior valor foi o {max(valores)} que estavam na posição {valores.index(max(valores))}')
print(f'O menor valor foi o {min(valores)} que estavam na posição {valores.index(min(valores))}')
valores.sort()
print(f'{valores}')