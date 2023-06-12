
n = 0
cont = 0
sum = 0
media = 0
op = 's'
maior = 0


while op == 's':

    n = int(input('Digite um número: '))

    if n > maior:
        maior = n


    cont = cont + 1
    sum = n + sum


    op = str(input('Deseja continuar? '))

    media = (sum/cont)


print('A média entre os números digitados é {}\nE a soma entre eles é {}\nE o maior entre eles é: {}'.format(media,sum,maior))