from conta import *

conta01 = Conta(46175, 'Danilo', 500, 1000000)
cliente = Cliente('João', 'Oliveira', '1111111111-1')

conta02 = Conta(45175, 'Sônia', 200, 1000000)
conta03 = Conta('123-4',cliente.nome, 120.0, 1000.0)

conta01.transfere_para(conta02,200)
conta01.deposita(500)
conta01.transfere_para(conta02,50)
conta01.saca(50)


print()

#print(conta03.titular)
#print(cliente.nome)


