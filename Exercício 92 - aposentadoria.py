nome = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
idade = 2023 - nascimento
carteira = int(input('Carteira de Trabalho (0 não tem): '))

dados = {}

dados['nome'] = nome
dados['idade'] = idade

if carteira != 0:
    contratacao = int(input('Ano de contratação: '))
    salario = float(input('Salário: R$ '))
    aposentadoria = (contratacao - nascimento  + 35)
    dados['ctps'] = carteira
    dados['contratação'] = contratacao
    dados['salário'] = salario
    dados['aposentadoria'] = aposentadoria
elif carteira == 0:
    dados['ctps'] = 0

print('-='*50)
print(dados)

for k, v in dados.items():
    print(f'{k} tem o valor {v}')


