import numpy as np
from Class_integral import Matematica
import math

# Definir a função
def f(x):
    return math.sin(x) / x

# Avaliar a função para valores de x próximos a 0
x = 0.000001
dx = 0.000001

valores = []

while x <= 0.1:
    valores.append(f(x))
    x += dx

# Imprimir os valores obtidos
print(valores)

# Estimar o limite
limite = sum(valores) / len(valores)
print("O limite de sin(x) / x quando x tende a 0 é", limite)


#termo = (input('Digite uma função qualquer: '))

#subtermo = termo.split('**') #aqui ele exclui o ** e pega o x e o expoente em uma lista

#print(subtermo)

#coeficiente = subtermo[0]
#variavel = subtermo[1][0]

#if len(subtermo[1]) >= 2:
 #   expoente = subtermo[1][1]
#else:
 #   expoente = ''
#
#for c in funcao:

 #   expoente_caido = funcao[3] - 1

#print(variavel)
#print(expoente)










#m1 = Matematica(3, 4, 0.00001, '4*i**2')
#m2 = Matematica(1, 10,0.00001, 'i**10 + i + 5')
#m3 = Matematica(0, 1, 0.00001, 'i**2 + math.sqrt(i)')
#m4 = Matematica(1, -5, -0.00001, '(i+1)**(4)')

#m1.integral()
#m2.integral()
#m3.integral()
#m4.integral()




