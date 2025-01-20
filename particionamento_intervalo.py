import tkinter as tk
from tkinter import Label, Entry, Button, Toplevel, messagebox
import os
from library.gerar_pdf import PDF
from PIL import Image, ImageTk

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

    mostrar_resultado(resultado.strip())

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

    label_resultado = tk.Label(canvas, text=f"Alocação de Salas:\n{resultado}", justify="left", anchor="nw")
    label_id = canvas.create_window(0, 0, window=label_resultado, anchor="nw")

    def atualizar_scrollregion(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    label_resultado.bind("<Configure>", atualizar_scrollregion)

    Button(nova_janela, text="Baixar PDF", command=lambda: gerar_pdf(resultado)).pack(pady=10)

def gerar_pdf(resultado):
    pdf = PDF(resultado, diretorio_atual)
    pdf.criar_pdf()

janela = tk.Tk()
janela.title("Particionamento de Intervalos")

janela.geometry('960x540')
janela.resizable(False, False)

imagem = Image.open(diretorio_atual + "/imgs/particionamento-de-intervalos.png")
imagem_tk = ImageTk.PhotoImage(imagem)
label = Label(janela, image=imagem_tk).place(x=0, y=-235, relwidth=1, relheight=1)

Label(janela, text="Insira uma atividade por linha, separando o nome da atividade, a hora de início e a hora de término por vírgulas.\nExemplo:\nCálculo 1, 09:00, 10:30\nCálculo 2, 09:00, 10:30\n", font=('Arial', 11), justify="left").place(x=50, y=100)

entrada_atividades = tk.Text(janela, height=10, width=80)
entrada_atividades.place(x=50, y=200)

Button(janela, text="Calcular", command=calcular_interval_partitioning).place(x=50, y=400)

janela.mainloop()
