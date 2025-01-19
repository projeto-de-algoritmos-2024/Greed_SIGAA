import tkinter as tk
from tkinter import Tk, Label, Entry, Button, Frame, Toplevel, messagebox
import os, subprocess
from PIL import Image, ImageTk

def calcular_min_lateness():
    print("#")

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

janela.mainloop()