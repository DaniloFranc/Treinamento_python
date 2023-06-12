data = {}
nome = str(input('Nome do jogador: '))
data['nome'] = nome
partidas = int(input(f'Quantas partidas {nome} jogou? '))
goals = list()
total = 0

for c in range(0,partidas):
    n = int(input(f'Quantos gols na partida {c}? '))
    goals.append(n)
    total += n

data['gols'] = goals
data['total'] = total

print('-='*50)
print(data)
print('-='*50)

for k,v in data.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*50)

print(f'O jogador {data["nome"]} jogou {partidas} partidas.')

for k in range(0, len(goals)):
    print(f'    => Na partida {k}, fez {goals[k]} gols.')
print(f'Foi um total de {data["total"]} gols.')