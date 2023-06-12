
i = int(input('Digite um número: '))
n = 1
p = 1

while n != i+1:

    p = n*p
    n = n + 1
    print(p)
print('O fatorial do número é: {}'.format(p))

