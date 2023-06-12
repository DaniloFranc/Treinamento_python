import datetime

class Historico:

    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []
    def imprime(self):
        print(f'data abertura: {self.data_abertura}')
        print('transações: ')
        for t in self.transacoes:
            print('-', t)


class Cliente:

    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.dados = []

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print('Inicializando uma conta')
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico() #se eu faço isso eu acesso a classe Histórico


    def deposita(self, valor):

        self.saldo = self.saldo + valor
        self.historico.transacoes.append(f'depósito de {valor}')



    def saca(self, valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo = self.saldo - valor
            self.historico.transacoes.append(f'saque de {valor}')
            return True

    def extrato(self):
        print(f'numero: {self.numero} \nsaldo: {selfnumero}')
        self.historico.transacoes.append(f'tirou extrato - saldo de {self.saldo}')

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append(f'transferência de {valor} para conta {destino.numero}')
            return True

