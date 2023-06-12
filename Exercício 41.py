N = int(input('Digite o ano do seu nascimento: '))

if A <= 9:
    print('Categoria MIRIM')
elif 9 < A <= 14:
    print('Categoria INFANTIL')
elif 14 < A <= 19:
    print('Categoria JÚNIOR')
elif 19 < A <= 20:
    print('Categoria SÊNIOR')
elif A > 20:
    print('Categoria MASTER')
