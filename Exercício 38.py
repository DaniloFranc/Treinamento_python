N1 = int(input('Digite o primeiro número: '))
N2 = int(input('Digite o segundo número: '))

if N1 > N2:
    print('O maior valor é: {}!'.format(N1))
elif N2 > N1:
    print('O maior valor é {}!'.format(N2))
elif N1 == N2:
    print('Não existe valor maior, os dois são iguais!')