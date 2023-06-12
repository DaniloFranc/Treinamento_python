import tkinter as tk

def separar_numeros():
    lista_entrada = entrada.get()
    lista = lista_entrada.split(',')
    lista_pares = []
    lista_impares = []
    for numero in lista:
        if numero.strip():  # Verifica se a string não está vazia
        #   try:
                numero = int(numero.strip())
                if numero % 2 == 0:
                    lista_pares.append(numero)
                else:
                    lista_impares.append(numero)
        #    except ValueError:
         #       saida.config(text="Entrada inválida. Por favor, insira somente números separados por vírgula.")
          #      return
    saida.config(text="Lista de entrada: " + lista_entrada + "\n" +
                  "Lista de pares: " + str(lista_pares) + "\n" +
                  "Lista de ímpares: " + str(lista_impares))

app = tk.Tk()
app.title("Separador de números pares e ímpares")

entrada = tk.Entry(app)
entrada.pack()

botao = tk.Button(app, text="Separar números", command=separar_numeros)
botao.pack()

saida = tk.Label(app, text="")
saida.pack()

app.mainloop()
