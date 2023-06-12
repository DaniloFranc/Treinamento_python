class Number:

    def __init__(self,n):
        self.num = n

    def Fatorial(self):
        fat = 1
        for i in range(1, self.num+1):
            fat = fat*i
        return fat




a = int(input("Digite um número para calcular o fatorial: "))

f1 = Number(a)

n = f1.Fatorial()

print(n)

