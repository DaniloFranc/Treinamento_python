
c = 1
impar = 0
par = 0

while c < 5:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        par = par + 1
    else: impar = impar + 1

    c = c + 1


print('O número de números impar é: {}\nE o número de números par é: {}'.format(impar, par))
