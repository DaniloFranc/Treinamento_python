nome = str(input('Digite seu nome completo: '))

A = nome.upper()
B = nome.lower()
C = nome.count(' ')
D = len(nome) - C
E = nome.split()
F = E[0]
G = len(F)

print(' Nome com TODAS as letras maiúsculas: {} \n Nome com TODAS as letras minúsculas: {} \n Número de letras no nome: {} \n Número de letras no primeiro nome: {} '.format(A,B,D,G))