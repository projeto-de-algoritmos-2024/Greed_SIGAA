import tkinter as tk
from tkinter import Label, Text, Button, Toplevel, messagebox
import os
from library.gerar_pdf import PDF
from PIL import Image, ImageTk

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

    mostrar_resultado(resultado)

def mostrar_resultado(resultado):
    nova_janela = Toplevel(janela)
    nova_janela.title("Resultados")
    nova_janela.geometry("500x400")

    frame_resultado = tk.Frame(nova_janela)
    frame_resultado.pack(fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(frame_resultado)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frame_resultado, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.config(yscrollcommand=scrollbar.set)

    label_resultado = tk.Label(canvas, text=f"Tarefas Selecionadas:\n{resultado}", justify="left", anchor="nw")
    label_id = canvas.create_window(0, 0, window=label_resultado, anchor="nw")

    def atualizar_scrollregion(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    label_resultado.bind("<Configure>", atualizar_scrollregion)

    Button(nova_janela, text="Baixar PDF", command=lambda: gerar_pdf(resultado)).pack(pady=10)

def gerar_pdf(resultado):
    pdf = PDF(resultado, diretorio_atual)
    pdf.criar_pdf()

janela = tk.Tk()
janela.title("Agendamento de Intervalos")

janela.geometry('960x540')
janela.resizable(False, False)

imagem = Image.open(diretorio_atual + "/imgs/agendamento-de-intervalos.png")
imagem_tk = ImageTk.PhotoImage(imagem)
label = Label(janela, image=imagem_tk).place(x=0, y=-235, relwidth=1, relheight=1)

Label(janela, text="Insira uma tarefa por linha, separando o nome da tarefa, a hora de início e a hora de término por vírgulas.\nExemplo:\nTarefa 1, 08:00, 11:00\nTarefa 2, 11:00, 12:00\n", font=('Arial', 11), justify="left").place(x=50, y=100)

entrada_atividades = Text(janela, height=15, width=80)
entrada_atividades.place(x=50, y=200)

Button(janela, text="Calcular", command=calcular_interval_scheduling).place(x=50, y=470)

janela.mainloop()
