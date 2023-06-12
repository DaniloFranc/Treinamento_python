import matplotlib.pyplot as plt

# Lê o arquivo .dat usando o Python puro
with open('saida.dat', 'r') as file:
    lines = file.readlines()

# Separa as colunas
col1 = []
col2 = []
for line in lines:
    values = line.strip().split()
    try:
        # Tenta converter as strings em números
        col1.append(float(values[0]))
        col2.append(float(values[1]))
    except ValueError:
        # Se ocorrer um erro, passa para a próxima linha
        continue

# Faz o gráfico das colunas
plt.plot(col1, col2)
plt.xlabel('Coluna 1')
plt.ylabel('Coluna 2')
plt.title('Gráfico das duas primeiras colunas')
plt.show()