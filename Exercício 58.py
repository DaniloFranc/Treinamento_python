import random

n = 0
num = 1


while n != num:
    n = int(input('Advinhe o número que pensei: '))
    num = random.randint(0,10)

print('Você acertou o número que pensei foi {}'.format(num))

