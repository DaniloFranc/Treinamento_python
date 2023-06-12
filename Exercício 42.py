import math

a = float(input('Digite o primeiro lado do triângulo: '))
b = float(input('Digite o segundo lado do triângulo: '))
c = float(input('Digite o terceiro lado do triângulo: '))

if math.fabs(b - c) < a < (b + c) and math.fabs(a - c) < b < (a + c) and math.fabs(a - b) < c < (a + b):
    print('Os lados formam um triangulo')
    if a == b == c:
        print('O triângulo é equilátero')
    elif a == b or a == c or b == c:
        print('O triângulo é Isóceles')
    elif a != b or a != c or b != c:
        print('O triângulo é Escaleno')


else: print('Os lados não formam um triângulo')
