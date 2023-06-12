import random

N = int(input('Advinhe o número que pensei: '))

A = random.randint(0,5)

if N == A:
    print('Parabéns você advinhou o número que pensei foi {}'.format(A))
else: print('Tente novamente, o número que pensei foi {}'.format(A))

