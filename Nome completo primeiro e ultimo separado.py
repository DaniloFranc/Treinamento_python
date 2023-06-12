Nome = str(input('Digite seu nome completo: ')).strip()

Nome = Nome.split()
T = int(len(Nome)) - 1 # isso aqui eu nunca entendi, hoje eu entendo.


print('O primeiro nome é: {}\n O último nome é: {}'.format(Nome[0],Nome[T]))

