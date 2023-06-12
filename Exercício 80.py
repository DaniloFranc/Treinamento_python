n = 0
numbers = list()
max = 0
for c in range(0,5):

    n = int(input('Digite um número: '))

    if c == 0 or n > numbers[-1]:   #se o número for maior que o valor que está no último elemento
        numbers.append(n)
    else:
        pos = 0 #guardar esse conceito aqui!
        while pos < len(numbers):
            if n <= numbers[pos]:
                numbers.insert(pos, n) #guardar esse conceito aqui!
                break
            pos = pos + 1 #guardar esse conceito aqui!
print(numbers)



