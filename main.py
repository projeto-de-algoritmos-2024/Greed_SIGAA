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

    text_bemvindo = Label(root, text="Olá, bem-vindo ao SIGAA! 👋", font=('normal', 12), justify="left")
    text_bemvindo.place(x=50, y=100)

    text_explicacao = Label(root, text="Este aplicativo oferece três opções para organizar suas atividades:\n ✅ Agendamento de Intervalos: Seleciona tarefas que podem ser realizadas sem sobreposição de horário.\n ✅ Particionamento de Intervalos: Aloca atividades em salas sem conflitos de horário.\n ✅ Minimização de Atraso: Organiza tarefas com prazos de forma a minimizar os atrasos.", font=('normal', 11), justify="left")
    text_explicacao.place(x=50, y=150)

    text_escolha = Label(root, text="Escolha uma opção de agendamento:", font=('normal', 12), justify="left")
    text_escolha.place(x=50, y=250)

    agenda_intervalos = Button(root, text="Agendamento de Intervalos", command=abrir_interval_scheduling)
    agenda_intervalos.place(x=50, y=280)

    agenda_particoes = Button(root, text="Particionamento de Intervalos", command=abrir_partition_scheduling)
    agenda_particoes.place(x=50, y=320)

    minimiza_atrasos = Button(root, text="Minimizar Atraso", command=abrir_min_lateness_scheduling)
    minimiza_atrasos.place(x=50, y=360)

    root.mainloop()

if __name__ == "__main__":
    main()
