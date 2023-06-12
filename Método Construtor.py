class Gato:

    def __init__(self, nome):
        self.nome = nome
        print('Seu gatinho se chama', self.nome)



nome_gato = input('Digite o nome de seu gato: ')

g1 = Gato(nome_gato)

