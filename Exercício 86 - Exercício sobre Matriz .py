line1 = []
line2 = []
line3 = []
Matriz = []


for c in range(0,3):
    line1.append(int(input(f'Digite o valor para [0,{c}]: ')))

for c in range(0,3):
    line2.append(int(input(f'Digite o valor para [1,{c}]: ')))

for c in range(0,3):
    line3.append(int(input(f'Digite o valor para [2,{c}]: ')))

Matriz.append(line1[:])
Matriz.append(line2[:])
Matriz.append(line3[:])


#print(line1)
#print(line2)
#print(line3)
print('-='*50)
for i in range(0,3): #guardar como ele imprime a matriz
    for c in range(0,3):
        print(f'[{Matriz[i][c]}]',end='')
    print()

