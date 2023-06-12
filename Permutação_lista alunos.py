import random

n1 = str('João')
n2 = str('Pedro')
n3 = str('José')
n4 = str('Marta')

lista = [n1,n2,n3,n4]
random.shuffle(lista)

print('A ordem de apresentação será ')
print(lista)