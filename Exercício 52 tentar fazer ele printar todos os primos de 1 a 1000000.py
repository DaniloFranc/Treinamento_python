A = int(input('Digite um número: '))
N = 0

for c in range(1, 1000000):
   if A % c == 0:
        N = N + c




if N == A + 1:
    print('Esse número é primo!')

else: print('Esse número não é primo!')

