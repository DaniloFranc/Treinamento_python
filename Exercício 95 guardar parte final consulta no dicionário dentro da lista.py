data = {}
total = 0
listagem = list()
goals = list()
cont = 0
while True:

    total = 0
    data.clear()
    nome = str(input('Nome do jogador: '))
    data['nome'] = nome

    partidas = int(input(f'Quantas partidas {nome} jogou? '))


    for c in range(0, partidas):
        n = int(input(f'Quantos gols na partida {c}? '))
        goals.append(n)
        total += n



    data['gols'] = goals[:]
    goals.clear()
    data['total'] = total


    cont += 1
    listagem.append(data.copy())

    while True:
        q = str(input('Quer continuar? [S/N] '))
        if q in 'SNsn':
            break

        print('ERRO! Responda apenas S ou N.')
    if q in 'Nn':
        break
#print(listagem)

print('-='*30)
print('cod ', end='')
for i in data.keys():
    print(f'{i:<15}',end='')
print()
print('-'*40)

for k,v in enumerate(listagem):
    print(f'{k:>3} ',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-'*40)


while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar ) '))
    if busca == 999:
        break
    if busca >= len(listagem):
        print(f'ERRO! Não existe jogador com o código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {listagem[busca]["nome"]}: ')
        for i, g in enumerate(listagem[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')