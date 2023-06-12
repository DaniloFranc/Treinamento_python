a = {}
lst = []
menor = 1000
segundo_menor = 1000
terceiro_menor = 1000
name_low = ''
name_second_low = ''
name_third_low = ''
for i in range(int(input())):
    name = input()
    score = float(input())
    student = {'name': name, 'score': score}
    lst.append(student)


for k in lst:
    if k['score'] < menor:
        terceiro_menor = segundo_menor
        name_third_low = name_second_low
        segundo_menor = menor
        name_second_low = name_low
        menor = k['score']
        name_low = k['name']

    elif k['score'] < segundo_menor and k['score'] >= menor:
        terceiro_menor = segundo_menor
        name_third_low = name_second_low
        segundo_menor = k['score']
        name_second_low = k['name']

    elif k['score'] < terceiro_menor and k['score'] >= segundo_menor:
        terceiro_menor = k['score']
        name_third_low = k['name']

result = [name_second_low, name_third_low]
result.sort()

print(result[0])
print(result[1])