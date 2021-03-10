import os
import webbrowser
from modulo_instala_pacotes import instala_pacotes
instala_pacotes(os,webbrowser)
import PyPDF4
from flask import Flask, render_template, request, redirect
from zipfile import *
from datetime import date
from modulo_busca_dados import busca_dados
from modulo_analisa_duplicados import analisa_duplicados
from modulo_analisa_cruzamento_dados import analisa_cruzamento_dados
from modulo_limpeza import limpeza

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/resultado_analise")
def resultado_analise():
    lista_pdf,lista_xml = busca_dados(os,PyPDF4)

    if lista_pdf == False:
        return render_template('erro pdf desconhecido.html')
    elif lista_xml == False: 
        return render_template('erro pasta desconhecida.html')

    lista_duplicados,duplicado = analisa_duplicados(lista_pdf)
    deleta_xml,erro_xml,erro_par_desconhecido,resultados,erro_xml_desconhecido = analisa_cruzamento_dados(lista_pdf,lista_xml)

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
    if request.method == "POST":
        Nome_Do_Arquivo = request.form['Nome_Arquivo'].capitalize()  
    
    data_dia = date.today().day
    data_mes = date.today().month
    data_ano = date.today().year

    if data_dia < 10:
        data_dia = "0"+str(data_dia)
    if data_mes < 10:
        data_mes = "0"+str(data_mes)
    
    data_ano = str(data_ano)[2:]
    
    data_criacao = f" {data_dia}.{data_mes}.{data_ano}"

    Nome_Do_Arquivo = os.path.expanduser('~')+"/Desktop/" + Nome_Do_Arquivo + data_criacao + ".rar"

    with ZipFile(Nome_Do_Arquivo, "w") as arquivo_rar:
        diretorio = os.path.expanduser('~')+"/Desktop/Aprovada"
        for root, dirs, files in os.walk(diretorio):
            for file in files:
                arquivo_rar.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(diretorio, '..')))
        diretorio=(os.path.expanduser('~')+"/Desktop/RelLivroFiscalSaidaNFCe.pdf")
        arquivo_rar.write(os.path.join(root, diretorio), os.path.relpath(os.path.join(root, diretorio), os.path.join(diretorio, '..')))
        arquivo_rar.close

    return render_template('fim.html')

@app.route("/log")
def log():
    lista_pdf,lista_xml = busca_dados(os,PyPDF4)
    deleta_xml,erro_xml,erro_par_desconhecido,resultados,erro_xml_desconhecido = analisa_cruzamento_dados(lista_pdf,lista_xml)

    return render_template('log.html',resultados=resultados)

@app.route("/deletar")
def deletar():
    lista_pdf,lista_xml = busca_dados(os,PyPDF4)
    deleta_xml,erro_xml,erro_par_desconhecido,resultados,erro_xml_desconhecido = analisa_cruzamento_dados(lista_pdf,lista_xml)
    limpeza(deleta_xml,os)

    return redirect('/resultado_analise')

app.run()
    