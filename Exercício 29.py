V = float(input('Digite a velocidade do carro: '))



if V <= 80:
    print('Você está no limite permitido')
else: print('Você foi multado por estar acima do limite em {} km/h e foi multado em {} R$!!'.format((V - 80),(V-80)*7))
