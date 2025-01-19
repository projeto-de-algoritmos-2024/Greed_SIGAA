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

Label(janela, text="Insira uma tarefa por linha, separando o nome da tarefa, a hora de início e a hora de término por vírgulas.\nExemplo:\nTarefa 1, 08:00, 11:00\nTarefa 2, 11:00, 12:00\n", font=('Arial', 11), justify="left").place(x=50, y=15)

entrada_atividades = tk.Text(janela, height=20, width=100)
entrada_atividades.place(x=15, y=100)

Button(janela, text="Calcular", command=calcular_interval_scheduling).place(x=400, y=450)

janela.mainloop()