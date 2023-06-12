n = int(input('Digite o número de termos da sequência: '))
i = 0
fn = 2
fa = 1
fb = 0
s = 0
a = 0

while i != n:

    if i > 0:
        fa = s #3
        fn = fb #5

    s = fa + fn #3 = s
    fb = s + fn #5 = fb
    i = i + 1
    print(f'{s}\n{fb}')
    a = s + fb





