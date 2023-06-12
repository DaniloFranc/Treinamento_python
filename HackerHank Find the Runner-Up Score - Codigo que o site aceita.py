n = int(input())
arr = list(map(int, input().split()))

lst = sorted(set(arr))

if len(lst) > 1:
    print(lst[-2])
else:
    print("Não há pontuações suficientes para encontrar o segundo colocado.")
