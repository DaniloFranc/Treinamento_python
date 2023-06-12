cont = 0


for c in range (1, 8):
    i = int(input('Digite o ano de nascimento da {} pessoa: '.format(c)))
    if  (2023 - i) > 21:
        cont = cont + 1
print('O número de pessoas que atingiram a maioridade é: {}'.format(cont))
print('O número de pessoas que não atingiu a maioridade é {}'.format(7-cont))