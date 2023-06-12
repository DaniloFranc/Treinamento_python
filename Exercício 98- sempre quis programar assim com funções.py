def contador(i,j,p):
    import time

    if i > j:
        p = p * -1
    if p < 0:
        print(f'Contagem de {i} até {j} de {-p} em {-p}:')
    else:
        print(f'Contagem de {i} até {j} de {p} em {p}:')

    for c in range(i, j+p, p):
        time.sleep(0.2)
        print(f'{c} ', end='')
    print('FIM!')



contador(1,10,1)
contador(10,0,2)

print('Agora é sua vez de personalizar a contagem!')
c = int(input('Início: '))
n = int(input('Fim: '))
p = int(input('Passo: '))

contador(c,n,p)