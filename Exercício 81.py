q = 's'
numbers = list()
cont = 0
cont5 = 0

while q == 's':

    n = int(input('Digite um valor: '))
    numbers.append(n)
    q = str(input('Deseja continuar? '))
    cont = cont + 1
    if q == 'n':
        break

numbers.sort(reverse=True)

print(f'Os valores em ordem decrescente são {numbers}\nVocê digitou {cont} elementos')

for c in range(0,len(numbers)):
    if numbers[c] == 5:
        cont5 = cont5 + 1

if cont5 != 0:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
