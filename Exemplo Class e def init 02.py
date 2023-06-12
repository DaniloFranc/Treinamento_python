class Operacoes:

    def __init__(self, a, b):
        self.soma = (a + b)
        self.subtracao = (a - b)


a = 4
b = 5
x = Operacoes(4, 5)

print(x.soma,x.subtracao)

