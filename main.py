import PyPDF2
import os

def mesclador_pdf():
    merger = PyPDF2.PdfMerger() #mesclador
    lista_arquivos = os.listdir("arquivos") #mostra os arquivos do diretorio
    lista_arquivos.sort()
    for arquivo in lista_arquivos:
        if ".pdf" in arquivo:
            merger.append(f"arquivos/{arquivo}")
    return merger.write("mesclagem_final.pdf")

mesclador_pdf()