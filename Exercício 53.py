frase = str(input('Digite uma frase: '))
N = len(frase) + 1

frase = frase.split()
frase = ''.join(frase)
frase01 = frase[::-1]
frase = frase.upper()
frase01 = frase01.upper()
print(frase01)

if frase == frase01:
    print('Essa frase é um palindromo!')
else: print('Essa frase não é um palindromo')



