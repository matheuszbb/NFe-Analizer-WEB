from flask import Flask, render_template, request, redirect
import webbrowser
import os
import PyPDF4
from zipfile import *
from datetime import date
from modulo_analisa_pdf import analisa_pdf 
from modulo_analisa_xml import analisa_xml
from modulo_analisa_tamanho import analisa_tamanho
from modulo_analisa_duplicados import analisa_duplicados
from modulo_analisa_cruzamento_dados import analisa_cruzamento_dados
from modulo_limpeza import limpeza

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/resultado_analise")
def resultado_analise():
    lista = analisa_pdf(os,PyPDF4)
    dicionario = analisa_xml(os)
    lista,dicionario = analisa_tamanho(lista,dicionario)
    lista_duplicados,duplicado = analisa_duplicados(lista)
    deleta_xml,erro_xml,erro_par_desconhecido,resultados,erro_xml_desconhecido = analisa_cruzamento_dados(lista,dicionario)

    for x in lista_duplicados:
        if x in erro_xml:
            erro_xml.remove(x)
    
    if len(erro_xml) == 0:
        erro_par_desconhecido = False

    if erro_par_desconhecido == True:
        return render_template('erro par desconhecido.html',erro_xml=erro_xml)

    if erro_xml_desconhecido == True:
        return render_template('erro xml desconhecido.html',deleta_xml=deleta_xml)

    return render_template('resultado.html',duplicado=duplicado,lista_duplicados=lista_duplicados)

@app.route("/finalizar", methods=["POST"])
def finalizar():  
    getUser = lambda: os.environ["USERNAME"] if "C:" in os.getcwd() else os.environ["USER"]
    usuario_pc = getUser()

    if request.method == "POST":
        Nome_Do_Arquivo = request.form['Nome_Arquivo'].capitalize()  
    
    data_criacao = f" {date.today().day}.{date.today().month}.{date.today().year}"

    Nome_Do_Arquivo ="C:/Users/"+usuario_pc+"/Desktop/" + Nome_Do_Arquivo + data_criacao + ".rar"

    with ZipFile(Nome_Do_Arquivo, "w") as arquivo_rar:
        diretorio = "C:/Users/"+usuario_pc+"/Desktop/Aprovada"
        for root, dirs, files in os.walk(diretorio):
            for file in files:
                arquivo_rar.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(diretorio, '..')))
        diretorio=("C:/Users/"+usuario_pc+"/Desktop/RelLivroFiscalSaidaNFCe.pdf")
        arquivo_rar.write(os.path.join(root, diretorio), os.path.relpath(os.path.join(root, diretorio), os.path.join(diretorio, '..')))
        arquivo_rar.close

    return render_template('fim.html')

@app.route("/log")
def log():
    lista = analisa_pdf(os,PyPDF4)
    dicionario = analisa_xml(os)
    lista,dicionario = analisa_tamanho(lista,dicionario)
    deleta_xml,erro_xml,erro_par_desconhecido,resultados,erro_xml_desconhecido = analisa_cruzamento_dados(lista,dicionario)

    return render_template('log.html',resultados=resultados)

@app.route("/deletar")
def deletar():
    lista = analisa_pdf(os,PyPDF4)
    dicionario = analisa_xml(os)
    lista,dicionario = analisa_tamanho(lista,dicionario)
    deleta_xml,erro_xml,duplicado1,resultados,erro_xml_desconhecido = analisa_cruzamento_dados(lista,dicionario)
    limpeza(deleta_xml,os)

    return redirect('/resultado_analise')

webbrowser.open('http://127.0.0.1:5000')
app.run()
    