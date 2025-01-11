import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime
import os

# Função para realizar o processo de recorte
def processar_pdf(caminho_pdf):
    try:
        # Abrindo o PDF original
        doc = fitz.open(caminho_pdf)

        # Definir variáveis de corte com base na seleção do RadioGroup
        if escolha_plataforma.get() == 1:  # MercadoLivre
            x0_p1, y0_p1, x1_p1, y1_p1 = 30, 140, 290, 570  # Página 1
            x0_p2, y0_p2, x1_p2, y1_p2 = 2, 0, 590, 755    # Página 2
        elif escolha_plataforma.get() == 2:  # OLX
            x0_p1, y0_p1, x1_p1, y1_p1 = 240, 20, 580, 520 # Página 1
            x0_p2, y0_p2, x1_p2, y1_p2 = 0, 20, 594, 792 # Página 2
        elif escolha_plataforma.get() == 3:  # Shopee
            x0_p1, y0_p1, x1_p1, y1_p1 = 0, 0, 310, 410 # Página 1
            x0_p2, y0_p2, x1_p2, y1_p2 = 0, 90, 580, 792 # Página 2

        # Primeira página - recorte
        page1 = doc[0]
        page1.set_cropbox(fitz.Rect(x0_p1, y0_p1, x1_p1, y1_p1))

        # Segunda página - recorte
        page2 = doc[1]
        page2.set_cropbox(fitz.Rect(x0_p2, y0_p2, x1_p2, y1_p2))

        # Salva temporariamente o PDF recortado
        doc.save("temp.pdf")

        # Criando um novo PDF para receber o conteúdo recortado
        doc1 = fitz.open()
        page = doc1.new_page()

        # Definindo as áreas da página superior e inferior
        r1 = fitz.Rect(0, 0, page.rect.width, page.rect.height / 2)  # Parte superior
        r2 = r1 + (0, page.rect.height / 2, 0, page.rect.height / 2)  # Parte inferior

        # Carregando o PDF temporário e adicionando as páginas recortadas
        src = fitz.open("temp.pdf")
        page.show_pdf_page(r1, src, 0, rotate=90)
        page.show_pdf_page(r2, src, 1, rotate=90)

        # Corrigindo o nome do arquivo para evitar caracteres inválidos
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        doc1.save(f"{timestamp}_Etiqueta.pdf")

        messagebox.showinfo("Tudo Certo!", "A etiqueta foi processada, recortada e salva!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Função para selecionar o arquivo PDF
def selecionar_arquivo():
    caminho_pdf = filedialog.askopenfilename(title="Selecione um arquivo PDF", filetypes=[("PDF files", "*.pdf")])
    if caminho_pdf:
        entrada_arquivo.delete(0, tk.END)
        entrada_arquivo.insert(0, caminho_pdf)


# Criação da interface gráfica usando Tkinter
root = tk.Tk()
root.title("Recortar e Processar PDF com PyMuPDF")

# Campo para selecionar o arquivo PDF
label_arquivo = tk.Label(root, text="Arquivo PDF:")
label_arquivo.pack()
entrada_arquivo = tk.Entry(root, width=50)
entrada_arquivo.pack()

# Botão para selecionar o arquivo PDF
botao_selecionar = tk.Button(root, text="Selecionar Arquivo PDF", command=selecionar_arquivo, bg="lightblue", fg="black")
botao_selecionar.pack(pady=10)

# Definir a escolha da plataforma com RadioGroup
escolha_plataforma = tk.IntVar(value=1)  # Variável que guarda a escolha (1=MercadoLivre, 2=OLX, 3=Shopee)

# Radio buttons para selecionar a plataforma
radio_ml = tk.Radiobutton(root, text="MercadoLivre", variable=escolha_plataforma, value=1)
radio_olx = tk.Radiobutton(root, text="OLX", variable=escolha_plataforma, value=2)
radio_shopee = tk.Radiobutton(root, text="Shopee", variable=escolha_plataforma, value=3)

radio_ml.pack()
radio_olx.pack()
radio_shopee.pack()

# Botão para processar o PDF
botao_processar = tk.Button(root, text="Processar PDF", command=lambda: processar_pdf(entrada_arquivo.get()), bg="lightgreen", fg="black")
botao_processar.pack(pady=10)

# Inicia o loop da interface gráfica
root.mainloop()
