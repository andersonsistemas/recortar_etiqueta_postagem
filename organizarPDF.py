import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter
from PIL import Image, ImageTk
import fitz  # PyMuPDF (melhor para renderizar miniaturas)
import json
import os

# pip install pymupdf
# pip install pillow PyPDF2

CONFIG_FILE = "pdf_config.json"

class PDFEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Organizador de PDF - Shopee")

        self.pdf_files = []  # lista com PDFs carregados
        self.page_frames = []  # widgets que mostram páginas

        self.frame_main = tk.Frame(root)
        self.frame_main.pack(fill="both", expand=True)

        # Botões principais
        toolbar = tk.Frame(root)
        toolbar.pack(fill="x")

        tk.Button(toolbar, text="Abrir PDFs", command=self.load_pdfs).pack(side="left", padx=5, pady=5)
        tk.Button(toolbar, text="Salvar PDF Final", command=self.save_pdf).pack(side="left", padx=5, pady=5)
        tk.Button(toolbar, text="Salvar Configuração", command=self.save_config).pack(side="left", padx=5, pady=5)
        tk.Button(toolbar, text="Carregar Configuração", command=self.load_config).pack(side="left", padx=5, pady=5)

        # Área de rolagem
        self.canvas = tk.Canvas(self.frame_main)
        self.scrollbar = tk.Scrollbar(self.frame_main, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Suporte para drag & drop
        self.drag_data = {"widget": None, "y": 0}

    def load_pdfs(self):
        paths = filedialog.askopenfilenames(filetypes=[("Arquivos PDF", "*.pdf")])
        if not paths:
            return
        for path in paths:
            self.add_pdf(path)

    def add_pdf(self, path):
        reader = PdfReader(path)
        for i in range(len(reader.pages)):
            self.add_page(path, i)

    def add_page(self, path, page_num):
        frame = tk.Frame(self.scrollable_frame, bd=2, relief="groove")
        frame.pack(fill="x", pady=2, padx=2)

        # Renderizar miniatura com PyMuPDF
        doc = fitz.open(path)
        pix = doc[page_num].get_pixmap(matrix=fitz.Matrix(0.4, 0.4))  # escala baixa para thumbnail
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        photo = ImageTk.PhotoImage(img)

        label_img = tk.Label(frame, image=photo)
        label_img.image = photo
        label_img.pack(side="left")

        var = tk.BooleanVar(value=True)
        chk = tk.Checkbutton(frame, text=f"{os.path.basename(path)} - Página {page_num+1}", variable=var)
        chk.pack(side="left", padx=5)

        # drag & drop events
        frame.bind("<ButtonPress-1>", self.on_drag_start)
        frame.bind("<ButtonRelease-1>", self.on_drag_stop)
        frame.bind("<B1-Motion>", self.on_drag_motion)

        self.page_frames.append((frame, path, page_num, var))

    def on_drag_start(self, event):
        self.drag_data["widget"] = event.widget
        self.drag_data["y"] = event.y_root

    def on_drag_stop(self, event):
        self.drag_data["widget"] = None
        self.drag_data["y"] = 0

    def on_drag_motion(self, event):
        widget = self.drag_data["widget"]
        if widget:
            dy = event.y_root - self.drag_data["y"]
            if abs(dy) > 10:  # arrastar mínimo
                index = [f[0] for f in self.page_frames].index(widget)
                new_index = index + (1 if dy > 0 else -1)
                if 0 <= new_index < len(self.page_frames):
                    self.page_frames[index], self.page_frames[new_index] = self.page_frames[new_index], self.page_frames[index]
                    self.reorder_frames()
                self.drag_data["y"] = event.y_root

    def reorder_frames(self):
        for frame, _, _, _ in self.page_frames:
            frame.pack_forget()
        for frame, _, _, _ in self.page_frames:
            frame.pack(fill="x", pady=2, padx=2)

    def save_pdf(self):
        writer = PdfWriter()
        for frame, path, page_num, var in self.page_frames:
            if var.get():
                reader = PdfReader(path)
                writer.add_page(reader.pages[page_num])
        if len(writer.pages) == 0:
            messagebox.showwarning("Aviso", "Nenhuma página selecionada!")
            return
        out_path = filedialog.asksaveasfilename(defaultextension=".pdf",
                                               filetypes=[("PDF files", "*.pdf")])
        if out_path:
            with open(out_path, "wb") as f:
                writer.write(f)
            messagebox.showinfo("Sucesso", f"PDF final salvo em:\n{out_path}")

    def save_config(self):
        config = []
        for _, path, page_num, var in self.page_frames:
            config.append({"path": path, "page_num": page_num, "selected": var.get()})
        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f, indent=2)
        messagebox.showinfo("Configuração", "Configuração salva com sucesso!")

    def load_config(self):
        if not os.path.exists(CONFIG_FILE):
            messagebox.showwarning("Erro", "Nenhuma configuração encontrada!")
            return
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
        # limpar
        for frame, _, _, _ in self.page_frames:
            frame.destroy()
        self.page_frames.clear()
        for item in config:
            self.add_page(item["path"], item["page_num"])
            self.page_frames[-1][3].set(item["selected"])

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFEditorApp(root)
    root.mainloop()