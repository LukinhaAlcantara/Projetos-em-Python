# ler tres nuneros 
# dizer qual deles e o maior e qual e o menor

primeiro = int(input('Primeiro numero: '))
segundo  = int(input('Segundo numero : '))
terceiro = int(input('Terceiro numero: '))

# Achando o maior número
maior = primeiro

if (segundo > maior):
        maior = segundo
if (terceiro > maior):
        maior = terceiro

print('Maior: ',maior)

# Achando o menor número
menor = primeiro

if (segundo < menor):
        menor = segundo
if (terceiro < menor):
        menor = terceiro

print('Menor: ',menor)
