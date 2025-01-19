import tkinter as tk
from tkinter import Tk, Label, Entry, Button, Frame, Toplevel, messagebox
import os, subprocess
from PIL import Image, ImageTk

def calcular_interval_scheduling():
    print("#")

janela = tk.Tk()
janela.title("Agendamento de Intervalos")
janela.geometry('960x540')
janela.resizable(False, False)
Label(janela, text="Insira as tarefas (ex: Tarefa 1, 08:00, 11:00):").pack()
entrada_tarefas = tk.Text(janela, height=10, width=40)
entrada_tarefas.pack()
Button(janela, text="Calcular", command=calcular_interval_scheduling).pack()
label_resultado = Label(janela, text="")
label_resultado.pack()
janela.mainloop()