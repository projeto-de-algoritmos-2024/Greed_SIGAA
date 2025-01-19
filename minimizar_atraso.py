import tkinter as tk
from tkinter import Tk, Label, Entry, Button, Frame, Toplevel, messagebox
import os, subprocess
from PIL import Image, ImageTk

def calcular_min_lateness():
    try:
        hora_inicio_h, hora_inicio_m = map(int, entrada_inicio.get().split(":"))
        hora_inicio = hora_inicio_h * 60 + hora_inicio_m
    except ValueError:
        messagebox.showerror("Erro de Entrada", "Formato do horário inicial: 'HH:MM' (ex: 08:00)")
        return
    
    trabalhos = entrada_atividades.get("1.0", tk.END).strip().split("\n")
    trabalhos_processados = []
    for trabalho in trabalhos:
        try:
            nome, duracao, prazo = trabalho.split(",")
            prazo_h, prazo_m = map(int, prazo.strip().split(":"))
            trabalhos_processados.append((nome.strip(), int(duracao.strip()), prazo_h * 60 + prazo_m))
        except ValueError:
            messagebox.showerror(
                "Erro de Entrada",
                "Formato: 'Trabalho, Duração, Prazo' (ex: Trabalho 1, 1, 18:00)"
            )
            return

    trabalhos_processados.sort(key=lambda x: x[2])
    tempo = hora_inicio
    agenda = []
    for trabalho in trabalhos_processados:
        inicio = tempo
        fim = tempo + trabalho[1] * 60
        tempo += trabalho[1] * 60
        
        if fim > trabalho[2]:
            atraso = fim - trabalho[2]
            horas_atraso = atraso // 60
            minutos_atraso = atraso % 60
            atrasado = f" (atraso de {horas_atraso}h {minutos_atraso}m)"
        else:
            atrasado = ""
        
        agenda.append((trabalho[0], inicio, fim, atrasado))

    resultado = "\n".join([f"{t[0]}: {t[1]//60:02}:{t[1]%60:02} - {t[2]//60:02}:{t[2]%60:02}{t[3]}" for t in agenda])
    label_resultado.config(text=f"Agenda de Trabalhos:\n{resultado}")


janela = tk.Tk()
janela.title("Minimizar Atraso")
janela.geometry('960x540')
janela.resizable(False, False)

Label(janela, text="Insira o horário que você pretente iniciar os trabalhos/tarefas (ex: 08:00):", font=('Arial', 11), justify="left").place(x=30, y=15)
entrada_inicio = tk.Entry(janela)
entrada_inicio.place(x=500, y=15)

Label(janela, text="Insira uma tarefa/trabalho por linha, separando o nome, o tempo de duração e a hora de término do prazo por vírgulas.\nExemplo:\nTrabalho 1, 1, 18:00\nTrabalho 2, 3, 18:00\n", font=('Arial', 11), justify="left").place(x=30, y=45)
entrada_atividades = tk.Text(janela, height=20, width=100)
entrada_atividades.place(x=15, y=130)

Button(janela, text="Calcular", command=calcular_min_lateness).place(x=400, y=480)

label_resultado = tk.Label(janela, text="", justify="left")
label_resultado.place(x=15, y=510)

janela.mainloop()