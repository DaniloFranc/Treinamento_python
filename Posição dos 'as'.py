frase = str(input('Digite uma frase: ')).strip()

frase = frase.upper()

N = frase.count('A')
M = frase.find('A')
O = frase.rfind('A')

print('A letra "a" aparece {} vezes'.format(N))
print('A letra "a" aparece na posição {} pela primeira vez'.format(M+1))
print('A letra "a" aparece na posição {} pela última vez'.format(O+1))




#quantas vezes aparece a trela 'a'?

#Em que posição ela aparece a primeira vez?

#Em que posição ela aparece a última vez?