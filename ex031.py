# perguntar a distancia em km de uma viagem
# se a vaijem for ate 200km 
# se cobra 0.50 centavos por km
# caso for mais longa 
# se cobra 0.45

distancia = float(input("Qual a distancia que será percorrida: "))

if(distancia <= 200):
    valor_da_viajem = distancia * 0.50
    print('O valor da passagem para essa vaijem será de {:.2f}'.format(valor_da_viajem))

else:
    valor_da_viajem = distancia * 0.45
    print('O valor da pasagem dessa viajem será no valor de {:.2f}'.format(valor_da_viajem))
    
