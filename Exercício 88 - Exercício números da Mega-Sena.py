from random import sample
import time

n = 0
frase1 = 'JOGA NA MEGA SENA'

print('-'*50)
print(frase1.center(50))
print('-'*50)
n = int(input('Quantos jogos você quer que eu sorteie? '))
if n != 0:
    print('-='*3,end='')
    print(f' SORTEANDO {n} JOGOS ',end='')
    print(f'-='*3)


for i in range(0,n):
    sorteados = sample(range(0, 61), 6)
    print(f'Jogo {i+1}: {sorteados}')
    time.sleep(1)

print('-='*4,end='')
print(f'< BOA SORTE! >',end='')
print(f'-='*3)
