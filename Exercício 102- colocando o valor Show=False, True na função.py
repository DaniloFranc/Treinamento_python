def fatorial(number,show=False):
    """
    fatorial(number, show=False)    
        -> Calcula o Fatorial de um número.
        :param number: O número a ser calculado.
        :param show: (opicional) Mostrar ou não a conta.
        :return: O valor do Fatorial de um número n.
    """""

    fat = 1

    for c in range(1, number + 1):
        fat = fat*c
    if show == True:
        for c in range(1,number):
            if c == 1:
                print(f'{c} ',end='')
            print(f'* {c+1} ',end='')

            if c == (number-1):
                print(f'= ', end='')
        print(fat)
    if show == False:
        print(fat)



#help(fatorial)
fatorial(5,show=True)


