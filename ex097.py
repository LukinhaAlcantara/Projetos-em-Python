def escreva(palavra):
    num = len(palavra)
    print('\033[1m-\033[m' * (num + 2))
    print("",palavra)
    print('\033[1m-\033[m' * (num + 2))
    
escreva(palavra = str(input("Qual a palavra: ")))