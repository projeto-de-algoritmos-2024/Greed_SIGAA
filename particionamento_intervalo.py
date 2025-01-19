import tkinter as tk
from tkinter import Tk, Label, Entry, Button, Frame, Toplevel, messagebox
import os, subprocess
from PIL import Image, ImageTk
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from library.gerar_pdf import PDF

diretorio_atual = os.path.dirname(os.path.abspath(__file__))

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

    resultado = ""
    for i, sala in enumerate(salas):
        resultado += f"SALA {i+1}:\n"
        for atividade in sala:
            resultado += f"  {atividade[0]} ({atividade[1]//60:02}:{atividade[1]%60:02} - {atividade[2]//60:02}:{atividade[2]%60:02})\n"
        resultado += "\n"

    label_resultado.config(text=f"Alocação de Salas:\n{resultado.strip()}")

    gerar_pdf = PDF(resultado, diretorio_atual)
    Button(janela, text="Baixar pdf", command=lambda: gerar_pdf.criar_pdf()).place(x=450, y=300)



janela = tk.Tk()
janela.title("Particionamento de Intervalos")
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
janela.geometry(f"{largura_tela}x{altura_tela}+0+0")

Label(janela, text="Insira uma atividade por linha, separando o nome da atividade, a hora de início e a hora de término por vírgulas.\nExemplo:\nCálculo 1, 09:00, 10:30\nCálculo 2, 09:00, 10:30\n", font=('Arial', 11), justify="left").place(x=50, y=15)

entrada_atividades = tk.Text(janela, height=10, width=80)
entrada_atividades.place(x=15, y=100)

Button(janela, text="Calcular", command=calcular_interval_partitioning).place(x=300, y=300)

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