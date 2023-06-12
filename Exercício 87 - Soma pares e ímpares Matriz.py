line1 = []
line2 = []
line3 = []
Matriz = []
pair = 0
odd = 0
bigger = 0
somater = 0

for c in range(0,3):
    line1.append(int(input(f'Digite o valor para [0,{c}]: ')))

for c in range(0,3):
    line2.append(int(input(f'Digite o valor para [1,{c}]: ')))

for c in range(0,3):
    line3.append(int(input(f'Digite o valor para [2,{c}]: ')))

Matriz.append(line1[:])
Matriz.append(line2[:])
Matriz.append(line3[:])

for i in range(0,3):
    for c in range(0,3):
        if Matriz[i][c] % 2 == 0:
            pair = pair + Matriz[i][c]
        else:
            odd = odd + Matriz[i][c]

for c in range(0,3):
    if Matriz[1][c] > bigger:
        bigger = Matriz[1][c]

for i in range(0, 3):
    somater = Matriz[i][2] + somater

print(f'A soma dos valores da terceira coluna é: {somater}')
print(f'O maior valor da segunda linha é: {bigger}')
print(f'A soma de todos os valores pares digitados é: {pair}')
print(f'A soma de todos os valores ímpares digitados é: {odd}')


#print('-='*50)
for i in range(0,3): #guardar como ele imprime a matriz
    for c in range(0,3):
        print(f'[{Matriz[i][c]}]',end='')
    print()
