


numbers = tuple(int(input('Digite um número: ')) for c in range(0,4))

#numbers = ((int(input('Digite um número: '))),(int(input('Digite um número: '))),
#(int(input('Digite um número: '))),(int(input('Digite um número: '))))

print(f'O número 9 aparece {numbers.count(9)} vezes.')

if 3 in numbers:
    print(f'O valor 3 apareceu na {numbers.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')

print('Os valores pares digitados foram: ',end='')
for c in numbers:

    if c % 2 == 0:
        print(f'{c} ', end='')



