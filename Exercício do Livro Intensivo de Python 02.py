
names = [str(input('Digite o nome de uma pessoa: ')) for c in range(0,4)]

print(f'Saudações {names[0].title()}\nSaudações {names[1].title()}\nSaudações {names[2].title()}\nSaudações {names[3].title()}')

for c in range(0,4):
    names[c] = 'jão'

print(f'Saudações {names[0].title()}\nSaudações {names[1].title()}\nSaudações {names[2].title()}\nSaudações {names[3].title()}')

