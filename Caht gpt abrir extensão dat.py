import matplotlib.pyplot as plt

# ler dados do arquivo .dat
data = []
with open("saida.dat", "r") as f:
    for line in f:
        if not line.startswith("T"):
            values = line.split()
            if len(values) >= 2:
                x, y = map(float, values[:2])
                data.append((x, y))

# extrair valores de x e y dos dados lidos
x = [row[0] for row in data]
y = [row[1] for row in data]

# plotar gráfico
plt.plot(x, y, "o-")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Gráfico de X vs Y")
plt.show()