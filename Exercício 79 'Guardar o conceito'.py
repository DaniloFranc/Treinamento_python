
q = 's'

numbers = list()

while q != 'n':

    n = int(input('Digite um valor: '))

    if n not in numbers:
        numbers.append(n)
        print('Valor adicionado com sucesso...')

    else:
        print('Valor duplicado! Não vou adicionar...')

    q = str(input('Quer continuar? '))

print(numbers)

