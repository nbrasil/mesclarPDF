import PyPDF2
import os

merger = PyPDF2.PdfMerger() #mesclador

lista_arquivos = os.listdir() #mostra os arquivos do diretorio

for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        merger.append(f"arquivos/{arquivo}")

merger.write("mesclagem_final.pdf")