lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')  # isto é uma tupla #ela pode ser feita com ou sem ()
#Tuplas sao IMUTAVEIS
print(lanche[:3])
# as tuplas diferentes dos vetores podem ser atribuidas com dados com tipos diferentes
pessoa = ('Gustavo', 39, 'M', 99.89)

# tem 3 tipos diferentes de usar o for com a tupla

for comida in lanche:
    print(comida)

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')