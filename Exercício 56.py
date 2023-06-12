
S = 0
i = 0
c = 0
for n in range(1,5):

    nome = str(input('Digite o nome da {} pessoa: '.format(n)))
    idade = int(input('Digite a idade da {} pessoa: '.format(n)))
    sexo = str(input('Digite o sexo da pessoa de número {}: '.format(n)))
    S = (S + idade)

    if n == 1 and sexo == 'm':  #aqui ele armazena o primeiro valor do laço
        i = idade
    if sexo == 'm' and idade > i:  #aqui ele compara o primeiro valor do laço e vê se é maior
        i = idade

    if sexo == 'f' and idade < 20:
        c = c + 1

M = S/4


print(' A média das idades é: {}!\n O homem mais velho tem {} anos\n O número de mulheres que têm menos de 20 anos é: {}!'.format(M, i, c))