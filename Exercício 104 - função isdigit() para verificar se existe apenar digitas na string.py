def leiaint(mensagem='Digite um número inteiro: '):

    while True:
        numero_str = input(mensagem)
        if numero_str.isdigit():
            return int(numero_str)
        else:
            print('ERRO! Digite um número inteiro válido.')



n = leiaint('Digite um número: ')

print(f'Você acabou de digitar o número {n}')