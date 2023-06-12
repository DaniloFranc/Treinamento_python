from random import randint
import time

colocados = {}

for c in range(0,4):

    n = randint(1,6)
    print(f'O Jogador {c+1} tirou {n}')
    time.sleep(1)
    colocados[f'Jogador{c}'] = n

#ordenado_por_valor = dict(sorted(colocados.items(), key=lambda item: -item[1]))
ordenado_por_valor = dict(sorted(colocados.items(), key=lambda item: -item[1]))

print('Ranking dos jogadores:')
i = 1
for k,v in ordenado_por_valor.items():

    print(f'{i}° lugar: {k} com {v}')
    i = i + 1