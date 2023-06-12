def escreva(frase):

    n = len(frase)
    print('~'*(n+4))
    print(f'{frase.center(n+4," ")}')
    print('~' * (n + 4))


f = str(input('Digite sua mensagem: '))

escreva(f)
