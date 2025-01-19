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
Label(janela, text="Insira os trabalhos (ex: Trabalho 1, 1, 18:00):").pack()
entrada_trabalhos = tk.Text(janela, height=10, width=40)
entrada_trabalhos.pack()
Button(janela, text="Calcular", command=calcular_min_lateness).pack()
label_resultado = Label(janela, text="")
janela.mainloop()