D = float(input('Digite a quilometragem da sua viagem: '))

if D <= 200:
    print('O preço da sua passagem será: {}'.format(D*0.5))
else: print('O preço da sua passagem será: {}'.format(D*0.45))