cont = 0

for c in range (1, 7):
    i = int(input('Digite um número: '))

    if i % 2 == 0:
        cont = i + cont

print(cont)