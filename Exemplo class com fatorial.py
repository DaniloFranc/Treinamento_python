class fatorial:

    def __init__(self, number):
        fat = 1
        for c in range(1,number+1):
            fat = fat*c
        self.f  = fat



a = 6
x = fatorial(a)

print(x.f)
