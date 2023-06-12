Nome = str(input('Digite o seu nome completo: ')).strip()

#N = Nome.split()

Nome = Nome.upper()
A = Nome.find('SILVA')

#print(A)

if A != -1:
    print('Verdadeiro')
else:
    print('Falso')


