import random

linha = '=-'*50
linha02 = '-'*50
print(linha)
print('VAMOS JOGAR PAR OU ÍMPAR')
print(linha)
S = 0
i = random.randint(1, 10)
A = ''
vitorias = 0
while True:
    n = int(input('Diga um valor: '))
    PI = str(input('Par ou Impar? [p/i] '))
    s = n + i

    if s % 2 == 0:
        print(f'Você jogou {n} e o computador {i}. Total de {s} e deu PAR\n{linha02}')
        A = 'p'
    else:
        print(f'Você jogou {n} e o computador {i}. Total de {s} e deu IMPAR\n{linha02}')
        A = 'i'
    if PI == A:
        vitorias = vitorias + 1
    else:
        print(f'Você PERDEU!\n{linha}\nGAME OVER! Você venceu {vitorias} vezes.')
        break