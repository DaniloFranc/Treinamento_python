

list = list()
maior = 0
max = 0
min = 10**1000
index = 0


for c in range(0,5):
    list.append(int(input(f'Digite um valor para a posição {c}:  ')))

max = list[0]

for c in range(0,5):

    if  list[c] >= max:
        max = list[c]
    if list[c] < min:
        min = list[c]

print(f'Você digitou os valores {list}')
print(f'O maior valor digitado foi {max}',end='')
print(' Na posição ',end='')

for i, v in enumerate(list):
    if v == max:
        print(f'{i}...',end='')

print(f'\nO menor valor digitado foi {min}',end='')
print(' Na posição ',end='')

for i, v in enumerate(list):
    if v == min:
        print(f'{i}...',end='')




#    print(list[c])

