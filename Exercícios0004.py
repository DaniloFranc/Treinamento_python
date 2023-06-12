import random
#n1 = str(input('Primeiro aluno: '))
#n2 = str(input('Primeiro aluno: '))
#n3 = str(input('Primeiro aluno: '))
#n4 = str(input('Primeiro aluno: '))
n1 = str('João')
n2 = str('Pedro')
n3 = str('José')
n4 = str('Marta')

lista = [n1,n2,n3,n4]
e = random.choice(lista)

print('{}'.format(e))