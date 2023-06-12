V = float(input('Digite o valor da casa que deseja comprar: '))
S = float(input(('Digite o salário do comprador: ')))
A = float(input('Em quantos anos deseja pagar? '))

P = (V/(A*12))

if P > (S*0.3):
    print('Você terá o empréstimo negado!')
elif P < (S*0.3):
    print('Você terá o empréstimo concedido!')



