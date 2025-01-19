import tkinter as tk
from tkinter import Tk, Label, Entry, Button, Frame, Toplevel, messagebox
import os, subprocess
from PIL import Image, ImageTk


def calcular_partition_scheduling():
    print("#")


janela = tk.Tk()
janela.title("Particionamento de Intervalos")
janela.geometry('960x540')
janela.resizable(False, False)

Label(janela, text="Insira uma atividade por linha, separando o nome da atividade, a hora de início e a hora de término por vírgulas.\nExemplo:\nCálculo 1, 09:00, 10:30\nCálculo 2, 09:00, 10:30\n", font=('Arial', 11), justify="left").place(x=50, y=15)

entrada_atividades = tk.Text(janela, height=20, width=100)
entrada_atividades.place(x=15, y=100)

Button(janela, text="Calcular", command=calcular_partition_scheduling).place(x=400, y=450)
janela.mainloop()