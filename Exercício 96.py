def área():
    frase = 'Controle de terrenos'
    print(frase.center(50, ' '))
    print('-'*50)
    L = float(input('LARGURA (m): '))
    C = float(input('COMPRIMENTO (m): '))
    A = L*C
    print(f'A área de um terreno de {L}X{C} é de {A}m².')



área()
