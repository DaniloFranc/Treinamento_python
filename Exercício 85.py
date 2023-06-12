temp = []
pair = []
odd = []
numbers = []

for c in range(0,7):

    temp.append(int(input(f'Digite {c+1}° valor: ')))

    if temp[0] % 2 == 0:
        pair.append(temp[:])
        pair.sort()
        temp.clear()
    else:
        odd.append(temp[:])
        odd.sort()
        temp.clear()


numbers.append(pair[:])
numbers.append(odd[:])

print(f'Os valores pares digitados foram: {numbers[0]}')
print(f'Os valores ímpares digitados foram: {numbers[1]}')


#print(numbers)
#print(pair)
#print(odd)