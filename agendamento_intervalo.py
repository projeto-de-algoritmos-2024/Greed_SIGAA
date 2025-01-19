import tkinter as tk
from tkinter import Tk, Label, Entry, Button, Frame, Toplevel, messagebox
import os, subprocess
from PIL import Image, ImageTk
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from library.gerar_pdf import PDF

diretorio_atual = os.path.dirname(os.path.abspath(__file__))

def calcular_interval_scheduling():
    tarefas = entrada_atividades.get("1.0", tk.END).strip().split("\n")
    tarefas_processadas = []
    for tarefa in tarefas:
        try:
            nome, inicio, fim = tarefa.split(",")
            inicio_h, inicio_m = map(int, inicio.strip().split(":"))
            fim_h, fim_m = map(int, fim.strip().split(":"))
            tarefas_processadas.append((nome.strip(), inicio_h * 60 + inicio_m, fim_h * 60 + fim_m))
        except ValueError:
            messagebox.showerror("Erro de Entrada", "Formato: 'Tarefa, Hora de Início, Hora de Término' (ex: Tarefa 1, 08:00, 11:00)")
            return

    tarefas_processadas.sort(key=lambda x: x[2])
    tarefas_selecionadas = []
    ultima_hora_fim = 0
    for tarefa in tarefas_processadas:
        if tarefa[1] >= ultima_hora_fim:
            tarefas_selecionadas.append(tarefa)
            ultima_hora_fim = tarefa[2]

    resultado = "\n".join([f"{t[0]} ({t[1]//60:02}:{t[1]%60:02} - {t[2]//60:02}:{t[2]%60:02})" for t in tarefas_selecionadas])
    label_resultado.config(text=f"Tarefas Selecionadas:\n{resultado}")

    gerar_pdf = PDF(resultado, diretorio_atual)
    Button(janela, text="Baixar pdf", command=lambda: gerar_pdf.criar_pdf()).place(x=450, y=300)

janela = tk.Tk()
janela.title("Agendamento de Intervalos")

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
janela.geometry(f"{largura_tela}x{altura_tela}+0+0")

Label(janela, text="Insira uma tarefa por linha, separando o nome da tarefa, a hora de início e a hora de término por vírgulas.\nExemplo:\nTarefa 1, 08:00, 11:00\nTarefa 2, 11:00, 12:00\n", font=('Arial', 11), justify="left").place(x=50, y=15)

entrada_atividades = tk.Text(janela, height=10, width=80)
entrada_atividades.place(x=15, y=100)

Button(janela, text="Calcular", command=calcular_interval_scheduling).place(x=300, y=300)

###
frame_resultado = tk.Frame(janela)
frame_resultado.place(x=10, y=350)

canvas = tk.Canvas(frame_resultado)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame_resultado, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.config(yscrollcommand=scrollbar.set)

label_resultado = tk.Label(canvas, text="", justify="left")
label_id = canvas.create_window(0, 0, window=label_resultado, anchor="nw")

def atualizar_scrollregion(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

label_resultado.bind("<Configure>", atualizar_scrollregion)

janela.mainloop()