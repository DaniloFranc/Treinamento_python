class Cubo:
    """
    Classe para calcular o cubo de um número
    """
    def __init__(self,valor): # método construtor da classe
        self.x = valor
        print('Objeto criado!')
    def calcula_cubo(self):
        cubo = self.x * self.x * self.x
        return 'Cubo calculado: ' + str(cubo)



teste = Cubo(6)
c = teste.calcula_cubo()

print(c)
