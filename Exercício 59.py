
a = 0
op = 0

while a != 1:
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    print(' [1] Somar\n [2] Multiplicar\n [3] Maior\n [4] Novos números\n [5] Sair do programa')
    op = int(input(' Digite a opção: '))

    if op == 1:
        print('A soma é: {}'.format(n1+n2))
        a = 1

    if op == 2:
        print('A multiplicação é: {}'.format(n1*n2))
        a = 1

    if op == 3 and n1 > n2:
        print('O maior número é: {}'.format(n1))
        print('O maior número é: {}'.format(n2))
        a = 1

    #if op == 4:
        #n1 = int(input('Digite o primeiro número: '))
        #n2 = int(input('Digite o segundo número: ')) sei lá por que se eu apagar isso aqui o programa funciona kkkk


    if op == 5:
        a = 1 and print('FIM')
