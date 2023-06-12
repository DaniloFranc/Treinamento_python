n0 = int(input('Digite o primeiro termo de sua PA: '))
r = int(input('Digite a razão de sua PA: '))
A = n0

for c in range (0, 10):
    if c == 0:
        print(A, end = " ")
        A = A + r

    else:
       print(A, end =" ")
       A = A + r


