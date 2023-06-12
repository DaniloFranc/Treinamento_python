from math import sqrt,pow

A = float(input('Digite o valor do cateto oposto em cm: '))
B = float(input('Digite o valor do cateto adjacente em cm: '))

S = pow(A,2) + pow(B,2)

H = sqrt(S)

print('O valor da hipotenusa é: {}'.format(int(H)))
