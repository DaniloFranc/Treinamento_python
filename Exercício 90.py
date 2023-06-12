situação = {}
Avg = 0
Name = 0
for c in range(0,1):
    Name = str(input('Nome: '))
    Avg = float(input(f'Média de {Name}: '))
    situação['Nome'] = Name
    situação['Média'] = Avg

    if Avg >= 6:
        situação['Resultado'] = 'Aprovado'
    else:
        situação['Resultado'] = 'Reprovado'

print(f'Nome é igual a {situação["Nome"]}\nMédia é igual a {situação["Média"]}\nSituação é igual a {situação["Resultado"]}')
#print(situação)