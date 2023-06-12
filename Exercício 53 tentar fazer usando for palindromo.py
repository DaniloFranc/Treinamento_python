frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[letra]  #aqui não é lista mas... serve pra string por que representa o index de letra na frase

print(junto, inverso)

if junto == inverso:
    print('Essa frase é um palindromo!')
else:
    print('Essa frase não é um palindromo')