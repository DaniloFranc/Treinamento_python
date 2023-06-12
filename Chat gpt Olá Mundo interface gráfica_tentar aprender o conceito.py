import tkinter as tk

def exibir_mensagem():
    label.config(text="Olá mundo!")

app = tk.Tk()
app.title("Meu primeiro programa com GUI")

label = tk.Label(app, text="", width=20, height=5)
label.pack()

botao = tk.Button(app, text="Exibir mensagem", command=exibir_mensagem)
botao.pack()

app.mainloop()
