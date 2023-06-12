N1 = float(input('Digite a primeira nota: '))
N2 = float(input('Digite a segunda nota: '))

M = (N1 + N2)/2

if M < 5.0:
    print('Reprovado!')
elif 5.0 <= M <= 6.9:
    print('Recuperação')
elif M >= 7.0:
    print('Aprovado')