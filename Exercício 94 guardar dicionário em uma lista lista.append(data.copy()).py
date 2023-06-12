
data = {}
lista = list()
soma = 0
media = 0

while True:

    data['Nome'] = str(input('Nome: '))
    data['Idade'] = int(input('Idade: '))

    while True:
        data['Sexo'] = str(input('Sexo: [M/F]'))
        if data['Sexo'] in 'MFmf':
            break

    soma = soma + data['Idade']

    lista.append(data.copy())

    while True:
        q = str(input('Quer continuar? [S/N]'))
        if q in 'SNsn':
            break

        print('ERRO! Responda apenas S ou N.')
    if q in 'Nn':
        break

media = soma/(len(lista))

print(f'- O grupo tem {len(lista)} pessoas')
print(f'- A média de idade é {media:.2f} anos')
print('- As mulheres cadastradas foram: ',end='')


for c in lista:
    if c['Sexo'] in 'fF':
        print(f'{c["Nome"]}, ',end='')
print('\n- Lista das pessoas que estão acima da média:')


for c in lista:
    if c['Idade'] >= media:
        print(f'\nnome = {c["Nome"]}; sexo = {c["Sexo"]}; idade = {c["Idade"]};\n',end='')
print('<< ENCERRADO >>')
