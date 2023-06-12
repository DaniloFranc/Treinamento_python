import numpy as np
import math

class Matematica:

    def __init__(self, inicio, fim, passo, funcao):
        print('Numero cadastrado com sucesso!')
        self.inicio = inicio
        self.fim = fim
        self.passo = passo
        self.funcao = funcao

    def integral(self):

        numbers = np.arange(self.inicio, self.fim, self.passo)
        sum = 0

        for i in numbers:
           # print(f'x: {i}')
            y = eval(self.funcao)
           # print(f'y: {y}')
            sum = sum + (self.passo * y)
            print(i);


        print(round(sum,5))
