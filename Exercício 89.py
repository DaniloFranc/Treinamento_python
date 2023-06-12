temp = []
student = []
q = 's'
cont = 0
average = 0
avg = []

while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Nota 1: ')))
    temp.append(int(input('Nota 1: ')))
    average = (temp[1] + temp[2])/2

    avg.append(average)

    student.append(temp[:])
    temp.clear()
    cont += 1

    q = str(input('Deseja continuar? [S/N] '))
    if q in 'Nn':
        break

for c in range(len(student)):
    print(f'{c}    {student[c][0]}      {avg[c]}')

while True:

    s = int(input('Mostar notas de qual aluno? (999 interrompe): '))
    for i in range(len(student)):
        if s == i:
            print(f'As notas de {student[i][0]} são {student[i][1]} e {student[i][2]}')

    if s == 999:
        break


