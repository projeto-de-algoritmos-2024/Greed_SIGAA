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
Label(janela, text="Insira as atividades (ex: Matemática, 08:00, 10:00):").pack()
entrada_atividades = tk.Text(janela, height=10, width=40)
entrada_atividades.pack()
Button(janela, text="Calcular", command=calcular_partition_scheduling).pack()
label_resultado = Label(janela, text="")
label_resultado.pack()
janela.mainloop()