def dobra(valores):
    i = 0
    while i < len(valores):
        valores[i] = valores[i]*2
        i = i + 1


numbers = [1,2,3,4,5,6,7,8,9,10]

dobra(numbers)
print(numbers)
