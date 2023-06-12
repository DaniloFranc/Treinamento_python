def sorteia(self):
    import random

    for c in range(0,5):
        a = random.randint(0, 10)
        self.append(a)


def somaPar(self):
    s = 0
    for c in range(0,len(self)):
        if self[c] % 2 == 0:
            s = self[c] + s
    print(f'A soma de todos os valores pares é: {s}.')




lista = []

sorteia(lista)

print(lista)

somaPar(lista)
