times = ('Palmeiras','Internacional','Fluminense','Corinthians','Flamengo','Athletico-PR','Atlético-MG','Fortaleza','São Paulo','América-MG','Botafogo','Santos','Goiás','Bragantino','Coritiba','Cuiabá','Ceará','Atletico-GO','Avaí','Juventude')

print('\nA lista de times do Brasileirão: ')
for c in range(0,20):
    print(f'{times[c]}   ', end='')


print('\nOs 5 primeiros colocados são: \n', end='')
for c in range(0,6):

    print(f'{times[c]}   ',end='')

print('\nOs 4 ultimos colocados são: \n', end='')
for c in range(19,15,-1):

    print(f'{times[c]}   ',end='')
print('\nO São Paulo está na posição {}'.format(times.index('São Paulo')))




