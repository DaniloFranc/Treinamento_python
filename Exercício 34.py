S = float(input('Digite o valor do seu salário: '))
A = S*0.1
B = S*0.15

if S > 1250:
    print('O seu aumento salarial será de {} R$'.format(A))
else: print('O seu aumento salarial será de {} R$'.format(B))