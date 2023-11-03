def contador(inicio, fim, passo):
    for c in range(inicio, fim, passo):
        print(f'{c}', end='->')
    
def escreva(palavra):
    num = len(palavra)
    print('\n')
    print('\033[1m-\033[m' * (num + 2))
    print("",palavra)
    print('\033[1m-\033[m' * (num + 2))
    
contador(inicio=1, fim=10, passo=1)
escreva(palavra='acabou')
contador(inicio=10, fim=0, passo=2)
escreva(palavra='acabou')
contador(inicio=int(input("INICIO: ")), fim=int(input('FIM: ')), passo=int(input('PASSO: ')))
escreva(palavra='acabou')