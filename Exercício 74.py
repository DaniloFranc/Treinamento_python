import random


maior = 0
menor = 0

numbers = tuple(random.randint(0,10) for c in range(5))

print('Os valores sorteados foram: ',end='')

for c in range(0,5):

    print(f'{numbers[c]} ',end='')

sorted_numbers = tuple(sorted(list(numbers)))
maior = sorted_numbers[4]
menor = sorted_numbers[0]

print(f'\nO maior valor sorteado foi: {maior}\nO menor valor sorteado foi: {menor}')
