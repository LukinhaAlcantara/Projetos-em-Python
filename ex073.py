time = ('Zero','Palmeiras','Internacional','Fluminense','Corinthians','Flamengo','AthleticoPR','AtleticoMG','Fortaleza','São Paulo','America-MG','Botafogo','Santos','Goiás','Red Bull Bragantino','Coritiba','Cuiabá-MT','Ceará','Atletico-GO','Avaí', 'Juventude')

print(f'Os 5 primeiros colocados na tabela do brasileirão são os {time[1:6]}')
print(f'Os ultimos quatros colocados são os {time[-4:]}')
print(sorted(time))
print(f'O flamengo esta na posição ', time.index('Flamengo'))