import tkinter as tk
from tkinter import Tk, Label, Entry, Button, Frame, Toplevel, messagebox
import os, subprocess
from PIL import Image, ImageTk


diretorio_atual = os.path.dirname(os.path.abspath(__file__))

def abrir_interval_scheduling():
    subprocess.run(['python3', diretorio_atual +'/agendamento_intervalo.py'])

def abrir_partition_scheduling():
    subprocess.run(['python3', diretorio_atual +'/agendamento_particao.py'])

def abrir_min_lateness_scheduling():
    subprocess.run(['python3', diretorio_atual +'/minimizar_atraso.py'])

def main():
    root = tk.Tk()
    root.title("SIGAA - Sistema Integrado de Gestão Ágil de Agendamentos")
    root.geometry('960x540')
    root.resizable(False, False)

    imagem = Image.open(diretorio_atual + "/img/SIGAA.png")
    imagem_tk = ImageTk.PhotoImage(imagem)
    label = Label(root, image=imagem_tk).place(x=0, y=-235, relwidth=1, relheight=1)

    text_escolha = Label(root, text="Escolha uma opção de agendamento:", font=('normal', 12), justify="left")
    text_escolha.place(x=100, y=130)

    agenda_intervalos = Button(root, text="Agendamento de Intervalos", command=abrir_interval_scheduling)
    agenda_intervalos.place(x=100, y=160)

    agenda_particoes = Button(root, text="Particionamento de Intervalos", command=abrir_partition_scheduling)
    agenda_particoes.place(x=100, y=200)

    minimiza_atrasos = Button(root, text="Minimizar Atraso", command=abrir_min_lateness_scheduling)
    minimiza_atrasos.place(x=100, y=240)

    root.mainloop()

if __name__ == "__main__":
    main()
