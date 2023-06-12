def maior(lista):
    import time
    maior = 0
    if lista == []:
        print('Foram informados 0 valores ao todo.')
        print('O maior valor informado foi 0' )
        print('-=' * 50)
    else:
        print('Analisando os valores passados...')
        for c in range(0,len(lista)):
            time.sleep(0.5)
            print(f'{lista[c]} ',end='')
        print(f'Foram informados {len(lista)} valores ao todo')
        for c in range(0,len(lista)):
            if lista[c] > maior:
                maior = lista[c]
        print(f'O maior valor informado foi {maior}.')
        print('-=' * 50)



l = [20,1,2,5,3,6000,1,0,10]
n = [900]
m = []
a = [4,7,0]
maior(m)
maior(n)
maior(a)
maior(l)