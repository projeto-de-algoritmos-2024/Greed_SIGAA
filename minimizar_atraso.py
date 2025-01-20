import tkinter as tk
from tkinter import Label, Entry, Button, Toplevel, messagebox
import os
from library.gerar_pdf import PDF
from PIL import Image, ImageTk

diretorio_atual = os.path.dirname(os.path.abspath(__file__))

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

    mostrar_resultado(resultado)

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

    label_resultado = tk.Label(canvas, text=f"Agenda de Trabalhos:\n{resultado}", justify="left", anchor="nw")
    label_id = canvas.create_window(0, 0, window=label_resultado, anchor="nw")

    def atualizar_scrollregion(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    label_resultado.bind("<Configure>", atualizar_scrollregion)

    Button(nova_janela, text="Baixar PDF", command=lambda: gerar_pdf(resultado)).pack(pady=10)

def gerar_pdf(resultado):
    pdf = PDF(resultado, diretorio_atual)
    pdf.criar_pdf()

janela = tk.Tk()
janela.title("Minimizar Atraso")

janela.geometry('960x540')
janela.resizable(False, False)

imagem = Image.open(diretorio_atual + "/imgs/agendamento-para-minimizar-atrasos.png")
imagem_tk = ImageTk.PhotoImage(imagem)
label = Label(janela, image=imagem_tk).place(x=0, y=-235, relwidth=1, relheight=1)

Label(janela, text="Insira o horário que você pretente iniciar os trabalhos/tarefas (ex: 08:00):", font=('Arial', 11), justify="left").place(x=50, y=100)
entrada_inicio = tk.Entry(janela)
entrada_inicio.place(x=520, y=100)

Label(janela, text="Insira uma tarefa/trabalho por linha, separando o nome, o tempo de duração e a hora de término do prazo por vírgulas.\nExemplo:\nTrabalho 1, 1, 18:00\nTrabalho 2, 3, 18:00\n", font=('Arial', 11), justify="left").place(x=50, y=140)

entrada_atividades = tk.Text(janela, height=10, width=80)
entrada_atividades.place(x=50, y=230)

Button(janela, text="Calcular", command=calcular_min_lateness).place(x=50, y=420)

janela.mainloop()
