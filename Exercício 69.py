linha = '-'*50
frase = 'Cadastre uma pessoa'
q = ''
cont = 0
homens = 0
mulheres = 0
while True:


    print(f'{linha}\n{frase.center(50)}\n{linha}')
    i = int(input('Idade: '))
    s = str(input('Sexo: [m/f]'))

    while s != 'm' and s != 'f':
        s = str(input('Sexo: [m/f]'))

    q = ''

    if i > 18:
        cont = cont + 1
    if s == 'm':
        homens = homens + 1
    elif s == 'f' and i < 20:
        mulheres = mulheres + 1

    while q != 's' and q != 'n':
        q = str(input('Quer continuar? '))

    if q == 'n':
        break
print(f'Total de pessoas com mais de 18 anos: {cont}\nAo todo temos {homens} cadastrados\nE temos {mulheres} mulheres com menos de 20 anos')
