from math import sin,cos,tan,pi

A = float(input('Digite o valor de um ângulo: '))

r = ((A*pi)/180)

s = sin(r)
c = cos(r)
t = tan(r)

print('O seno do ângulo é: {}, O cosseno do ângulo é {}, e a tangente do ângulo é: {}.'.format(s,c,t))
