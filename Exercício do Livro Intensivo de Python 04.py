list = [input('Digite o nome do convidado: ') for c in range(0,3)]

#numbers = tuple(random.randint(0,10) for c in range(5))

print(f'Olá {list[0]} você está convidado para o jantar!\nOlá '
      f'{list[1]} você está convidado para o jantar!\nOlá {list[2]} você está convidado para o jantar!')

print(f'{list[0]} não poderá comparecer')

list[0] = input('Digite o nome do convidado: ')
list.insert(0, 'José')
list.append('Maria')

print(f'Olá {list[0]} você está convidado para o jantar!\nOlá '
      f'{list[1]} você está convidado para o jantar!\nOlá {list[2]} você está convidado para o jantar!')

print(list)