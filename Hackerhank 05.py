if __name__ == '__main__':
    n = int(input())
    arr = str(input())

    arr = sorted(arr.split())
    i = arr.index((max(arr)))

if arr[i] != arr[i-1]:
    print(arr[i-1])

elif arr[i-1] == arr[i]:
    print(arr[i-2])

#print(arr.index(max(arr)))



    #print(sorted(list(set(arr)))[-2])