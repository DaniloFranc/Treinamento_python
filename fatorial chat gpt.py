def factorial(n):
    result = 1
    while n > 0:
        result = result * n
        n = n - 1
        print(result)
    return result

num = int(input("Enter a number: "))
print("The factorial of", num, "is", factorial(num))