class Conta:

    def __init__(self,titular,numero,saldo, limite):
        print('inicializando uma conta')
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo = self.saldo + valor



