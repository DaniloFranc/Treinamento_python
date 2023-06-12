def ficha(name,goals):

    if goals != '' and name == '':
        print(f'O jogador <desconhecido> fez {goals} no campeonato.')

    if goals == '' and name != '':
        print(f'O jogador {name} fez 0 no campeonato.')

    if name == '' and goals == '':
        print(f'O jogador <desconhecido> fez <desconhecido> no campeonato.')

    if name != '' and goals != '':
        print(f'O jogador {name} fez {goals} no campeonato.')




nome = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols: '))

ficha(nome,gols)