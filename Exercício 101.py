def voto(ano):

    idade = 2023 - ano
    if idade < 16:
        print(f'Com {idade} anos: NÃO VOTA.')
    if 16 < idade < 18:
        print(f'Com {idade} anos: VOTO NÃO É OBRIGATÓRIO.')
    if 18 < idade < 70:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
    if idade > 70:
        print(f'Com {idade} anos: VOTO OPICIONAL.')



print('-'*50)

a = int(input('Em que ano você nasceu? '))

voto(a)