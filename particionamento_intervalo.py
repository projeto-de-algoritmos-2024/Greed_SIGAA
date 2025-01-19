import tkinter as tk
from tkinter import Tk, Label, Entry, Button, Frame, Toplevel, messagebox
import os, subprocess
from PIL import Image, ImageTk

def calcular_interval_partitioning():
    atividades = entrada_atividades.get("1.0", tk.END).strip().split("\n")
    atividades_processadas = []
    for atividade in atividades:
        try:
            nome, inicio, fim = atividade.split(",")
            inicio_h, inicio_m = map(int, inicio.strip().split(":"))
            fim_h, fim_m = map(int, fim.strip().split(":"))
            atividades_processadas.append((nome.strip(), inicio_h * 60 + inicio_m, fim_h * 60 + fim_m))
        except ValueError:
            messagebox.showerror("Erro de Entrada", "Formato: 'Nome, Hora de Início, Hora de Término' (ex: Matemática, 08:00, 10:00)")
            return

    atividades_processadas.sort(key=lambda x: x[1])
    salas = []
    for atividade in atividades_processadas:
        alocada = False
        for sala in salas:
            if sala[-1][2] <= atividade[1]:
                sala.append(atividade)
                alocada = True
                break
        if not alocada:
            salas.append([atividade])

    resultado = "\n".join([f"Sala {i+1}: " + ", ".join([f"{a[0]} ({a[1]//60:02}:{a[1]%60:02} - {a[2]//60:02}:{a[2]%60:02})" for a in sala]) for i, sala in enumerate(salas)])
    label_resultado.config(text=f"Alocação de Salas:\n{resultado}")


janela = tk.Tk()
janela.title("Particionamento de Intervalos")
janela.geometry('960x540')
janela.resizable(False, False)

Label(janela, text="Insira uma atividade por linha, separando o nome da atividade, a hora de início e a hora de término por vírgulas.\nExemplo:\nCálculo 1, 09:00, 10:30\nCálculo 2, 09:00, 10:30\n", font=('Arial', 11), justify="left").place(x=50, y=15)

entrada_atividades = tk.Text(janela, height=20, width=100)
entrada_atividades.place(x=15, y=100)

Button(janela, text="Calcular", command=calcular_interval_partitioning).place(x=400, y=450)

label_resultado = Label(janela, text="", font=('Arial', 10), justify="left")
label_resultado.place(x=15, y=480)

janela.mainloop()