
linha = '-' * 50

while True:

    print(linha)
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n > 0:
        for c in range(1, 11):
            print(f'{n} x {c} = {n*c}')

    if n <= 0:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break
