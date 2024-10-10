import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime
from pathlib import Path

def processar_pdf(caminho_pdf):
    try:

        doc = fitz.open(caminho_pdf)  # Abre o documento PDF

        # Primeira página - recorte
        page1 = doc[0]  # Obtém a primeira página
        page1.set_cropbox(fitz.Rect(0, 0, 306, 370))  # Aplica o recorte

        # Segunda página - recorte
        page2 = doc[1]  # Obtém a segunda página
        page2.set_cropbox(fitz.Rect(2, 0, 580, 551))  # Aplica o recorte

        # Salva temporariamente o PDF recortado
        doc.save("temp_Shp.pdf")

        # Criando um novo PDF para receber o conteúdo recortado
        doc1 = fitz.open()  # Novo documento em branco
        page = doc1.new_page()  # Nova página no formato A4

        # Definindo as áreas da página superior e inferior
        r1 = fitz.Rect(0, 0, page.rect.width, page.rect.height / 2)  # Parte superior
        r2 = r1 + (0, page.rect.height / 2, 0, page.rect.height / 2)  # Parte inferior

        # Carregando o PDF temporário e adicionando as páginas recortadas
        src = fitz.open("temp_Shp.pdf")
        page.show_pdf_page(r1, src, 0, rotate=90)  # Página 1 rotacionada
        page.show_pdf_page(r2, src, 1, rotate=90)  # Página 2 rotacionada

        # Salva o PDF final com base na data e hora atual
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Formata a data/hora sem caracteres inválidos
        doc1.save(f"{timestamp}_Shopee.pdf")  # Salva com o nome formatado

        messagebox.showinfo("Sucesso", f"O arquivo {timestamp}_OLX.pdf foi processado e salvo com sucesso!")
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
root.title("Shopee Etiqueta - Recorte")

# Campo para selecionar o arquivo PDF
label_arquivo = tk.Label(root, text="Caminho do arquivo PDF:")
label_arquivo.pack()
entrada_arquivo = tk.Entry(root, width=50)
entrada_arquivo.pack()
botao_arquivo = tk.Button(root, text="Selecionar Arquivo", command=selecionar_arquivo,fg='white', bg='green')
botao_arquivo.pack()

# Botão para realizar o processamento
botao_processar = tk.Button(root, text="Recortar PDF", command=lambda: processar_pdf(entrada_arquivo.get()),fg='white', bg='red')
botao_processar.pack()

# Inicia o loop da interface gráfica
root.mainloop()