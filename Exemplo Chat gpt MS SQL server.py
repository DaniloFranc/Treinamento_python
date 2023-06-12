import pymssql
import csv

# Conexão com o MS SQL Server
conn = pymssql.connect(server='seu_servidor', user='seu_usuario',
                       password='sua_senha', database='seu_banco_de_dados')
cursor = conn.cursor()

# Criar tabela
cursor.execute("""
CREATE TABLE clientes (
    id INT PRIMARY KEY NOT NULL,SS
    primeiro_nome VARCHAR(50) NOT NULL
)
""")
conn.commit()

# Inserir dados na tabela
dados = [(1, 'João'), (2, 'Maria'), (3, 'Pedro')]
cursor.executemany("INSERT INTO clientes VALUES (%d, %s)", dados)
conn.commit()

# Escreva os dados em um arquivo CSV
cursor.execute("SELECT * FROM clientes")
with open('clientes.csv', 'w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerow([i[0] for i in cursor.description])  # escreve o cabeçalho
    escritor_csv.writerows(cursor)

# Fechar a conexão
conn.close()