a = ('zero','um','dois', 'três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

n = 0
c = 0

while True:

    if c == 0:
        n = int(input('Digite um número entre 0 e 20: '))
        c = c + 1

    if n >= 0 and n <= 20:
        break
    else:
        n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {a[n]}')