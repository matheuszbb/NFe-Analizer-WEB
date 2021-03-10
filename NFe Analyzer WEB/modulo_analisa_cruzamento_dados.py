def analisa_cruzamento_dados(lista_pdf,lista_xml,os):
  erro_xml_desconhecido = False
  erro_xml = []
  resultados = {}
  erro_par_desconhecido = False

  cont = 0
  for valor_pdf in lista_pdf:
    erros = True
    for valor_xml in lista_xml:
      if valor_pdf == valor_xml[0:44]:
        resultados[cont] = valor_pdf,valor_xml
        erros = False
    if erros == True:
      resultados[cont] = valor_pdf,"Par Não Encontrado"
      erro_xml.append(valor_pdf)
      erro_par_desconhecido = True
    cont = cont + 1 

  deleta_xml_txt = open(os.path.expanduser("~")+"/Documents/NFe Analyzer WEB/deleta_xml.txt","w")
  deleta_xml_txt.close()

  deleta_xml = []

  deleta_xml_txt = open(os.path.expanduser("~")+"/Documents/NFe Analyzer WEB/deleta_xml.txt","a")

  for valor_xml in lista_xml:
    erros = True
    cont = len(resultados)
    for valor_pdf in lista_pdf:
      if valor_xml[0:44] == valor_pdf:
        erros = False
    if erros == True:
      resultados[cont] = "Par Não Encontrado",valor_xml
      deleta_xml.append(valor_xml)
      deleta_xml_txt.write(valor_xml + "\n")
      erro_xml_desconhecido = True

  deleta_xml_txt.close()

  log = open(os.path.expanduser('~')+"/Documents/NFe Analyzer WEB/log.txt","w")
  log.close()

  for n in range(0,len(resultados)):
    log = open(os.path.expanduser('~')+"/Documents/NFe Analyzer WEB/log.txt","a")
    log.write(resultados[n][0]+ " , " + resultados[n][1] + "\n")
    log.close()

  return deleta_xml,erro_xml,erro_par_desconhecido,erro_xml_desconhecido