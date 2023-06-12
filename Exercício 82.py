numbers = list()
pares = list()
impares = list()

q = 's'


while q == 's':

    if q == 's':
        n = int(input('Digite um número: '))
        numbers.append(n)
    q = str(input('Deseja continuar? [s/n] '))
print('-='*50)
for c in range(0, len(numbers)):
    if numbers[c] % 2 == 0:
        pares.append(numbers[c])
    else:
        impares.append(numbers[c])

print(f'A lista completa é {numbers}\nA listade pares é {pares}\nA lista de impares é {impares}')
