import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
from tkinter import messagebox

class PDF:
    def __init__(self, resultado, diretorio):
        self.resultado = resultado
        self.diretorio = diretorio
        self.data_atual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    def criar_pdf(self):
        if not os.path.exists(self.diretorio + "/pdfs"):
            os.makedirs(self.diretorio + "/pdfs")

        caminho_pdf = self.diretorio + "/pdfs/resultado-agendamento-" + self.data_atual + ".pdf"

        c = canvas.Canvas(caminho_pdf, pagesize=letter)
        c.setFont("Helvetica", 12)
        
        c.drawString(100, 750, "Resultado do agendamento:")
        y = 730
        for linha in self.resultado.split("\n"):
            c.drawString(100, y, linha)
            y -= 20
        
        c.save()

        messagebox.showinfo("PDF Gerado", f"O PDF foi gerado com sucesso em: {caminho_pdf}")