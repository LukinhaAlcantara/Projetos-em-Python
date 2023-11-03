# crie um programa que faça o computador jogar jokempo com voce

import random
i = 'S'
while True:
    opções = ['pedra', 'papel', 'tesoura']

    computador = random.choice(opções)

    print('=-=-' * 5)
    print('\033[4;31m      JOKEMPO       \033[m')
    print('=-=-' * 5)
    print('\n   \033[1;31mPedra\033[m')
    print('\n   \033[1;31mPapel\033[m')
    print('\n   \033[1;31mTesoura\033[m')

    print('\n\033[1;32mFaça a sua escolha e tente a sorte contra o computador\033[m')

    escolha_usuario = str(input("Sua escolha: "))

    if(escolha_usuario == 'pedra' and computador == 'tesoura'):
        print("\033[1;32mParabens você venceu o computador\033[m")    #vitoria

    elif(escolha_usuario == 'pedra' and computador == 'papel'):
        print('\033[1;31mVocê fracassou o vencedor é o computador\033[m')  #derrota
        
    elif(escolha_usuario == 'pedra' and computador == 'pedra'):
        print('\033[1;34mNao houve vencedor pois os você pensou o mesmo que a maquina\033[m')  #empate
        
    elif(escolha_usuario == 'papel' and computador == 'pedra'):
        print('\033[1;32mPatabens você venceu o computador\033[m')
        
    elif(escolha_usuario == 'papel' and computador == 'tesoura'):
        print('\033[1;31mVocê fracassou o vencedor é o computador\033[m')
        
    elif(escolha_usuario == 'papel' and computador == 'papel'):
        print('\033[1;34mNão houve vencedor você pensou o mesmo que a maquina\033[m')
        
    elif(escolha_usuario == 'tesoura' and computador == 'papel'):
        print('\033[1;32mParabens você venceu o computador\033[m')
        
    elif(escolha_usuario == 'tesoura' and computador == 'pedra'):
        print('\033[1;31mVocê facrassou o vencedor e o computador\033[m')
        
    elif(escolha_usuario == 'tesoura' and computador == 'tesoura'):
        print('\033[1;34mNão houve vencedor você pensou igual a maquina\033[m')
    
    i = str(input('Voce deseja continuar [S/N] ')).upper()
    
    if i =='N':
        break