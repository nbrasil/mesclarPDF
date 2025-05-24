import os
import PyPDF2
import customtkinter as ctk
from tkinter import filedialog, messagebox

class PDFMergerApp:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Mesclador de PDFs")
        self.root.geometry("600x450")
        
        # Variável para armazenar os arquivos selecionados
        self.arquivos_selecionados = []
        
        # Configuração do tema
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Criar widgets da interface
        self.criar_interface()
        
    def criar_interface(self):
        # Frame principal
        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Botão para selecionar arquivos
        btn_selecionar = ctk.CTkButton(
            main_frame,
            text="Selecionar PDFs",
            command=self.selecionar_arquivos
        )
        btn_selecionar.pack(pady=10)
        
        # Frame rolável para os arquivos
        self.frame_arquivos = ctk.CTkScrollableFrame(
            main_frame,
            width=550,
            height=250
        )
        self.frame_arquivos.pack(pady=10)
        
        # Botão para mesclar
        ctk.CTkButton(
            main_frame,
            text="Mesclar PDFs",
            command=self.mesclar_pdfs,
            fg_color="#5cb85c",
            hover_color="#4cae4c"
        ).pack(pady=10)
    
    def selecionar_arquivos(self):
        caminhos = filedialog.askopenfilenames(
            title="Selecione os arquivos PDF",
            filetypes=(("Arquivos PDF", "*.pdf"), ("Todos os arquivos", "*.*"))
        )
        
        if caminhos:
            for caminho in caminhos:
                if caminho not in self.arquivos_selecionados:
                    self.arquivos_selecionados.append(caminho)
            self.atualizar_lista_arquivos()
    
    def atualizar_lista_arquivos(self):
        # Limpa o frame atual
        for widget in self.frame_arquivos.winfo_children():
            widget.destroy()
        
        # Adiciona cada arquivo como um item no frame
        for i, caminho in enumerate(self.arquivos_selecionados, 1):
            item_frame = ctk.CTkFrame(self.frame_arquivos, fg_color="transparent")
            item_frame.pack(fill="x", pady=2)
            
            # Nome do arquivo
            ctk.CTkLabel(
                item_frame,
                text=f"{i}. {os.path.basename(caminho)}",
                anchor="w",
                width=400
            ).pack(side="left", padx=5)
    
    def mesclar_pdfs(self):
        if not self.arquivos_selecionados:
            messagebox.showwarning("Aviso", "Nenhum arquivo PDF selecionado!")
            return
        
        try:
            # Criar o objeto merger
            merger = PyPDF2.PdfMerger()
            
            # Adicionar cada arquivo ao merger
            for arquivo in self.arquivos_selecionados:
                merger.append(arquivo)
            
            # Perguntar onde salvar o arquivo mesclado
            output_file = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=(("Arquivo PDF", "*.pdf"),),
                title="Salvar PDF mesclado como"
            )
            
            if output_file:
                # Escrever o arquivo mesclado
                merger.write(output_file)
                merger.close()
                
                messagebox.showinfo("Sucesso", f"PDFs mesclados com sucesso em:\n{output_file}")
                
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao mesclar os PDFs:\n{str(e)}")
        
        finally:
            if 'merger' in locals():
                merger.close()

if __name__ == "__main__":
    app = PDFMergerApp()
    app.root.mainloop()
