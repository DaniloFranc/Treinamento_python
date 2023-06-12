r = int(input('Digite a razão de sua PA: '))
n0 = int(input('Digite o primeiro termo de sua PA: '))

n = int(input('Digite o número de termos desejados: '))

i = 0
a = n0

while i != n:
    if i == 0:
        print(n0)
        i = i + 1
    a = a + r
    print(a)
    i = i + 1
print(a)

op = str(input('Deseja continuar? '))

if op == 's':
    n = int(input('Digite o número de termos desejados: '))
    i = 0
    while i != n:

        a = a + r
        print(a)
        i = i + 1
        if i == n:
            op = str(input('Deseja continuar? '))
            if op == 's':
                n = int(input('Digite o número de termos desejados: '))
                i = 0

else: i = i + 1



