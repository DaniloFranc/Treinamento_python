s = 0
cont = 0
n = 0

while True:
    n = int(input('Digite um valor (999 para parar): '))


    if n == 999:
        break
    s = s + n
    cont = cont + 1
print(f'A soma dos {cont} valores foi {s}')