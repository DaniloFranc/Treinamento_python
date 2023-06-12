class Fatorial():

    def __init__(self,number):
        self.number = number
       # print('Classe criada com sucesso')
    def fat(self):
        fat = 1
        for c in range(1, self.number + 1):
            fat = fat*c
        return fat




