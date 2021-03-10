def analisa_cruzamento_dados(lista_pdf,lista_xml):
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
      if valor_pdf != "88888888888888888888888888888888888888888888":
        resultados[cont] = valor_pdf,"Par Não Encontrado"
        erro_xml.append(valor_pdf)
        erro_par_desconhecido = True
    cont = cont + 1 

  deleta_xml = []
  for valor_xml in lista_xml:
    erros = True
    cont = len(resultados)
    for valor_pdf in lista_pdf:
      if valor_xml[0:44] == valor_pdf:
        erros = False
    if erros == True:
      if valor_xml != "99999999999999999999999999999999999999999999":
        resultados[cont] = "Par Não Encontrado",valor_xml
        deleta_xml.append(valor_xml)
        erro_xml_desconhecido = True

  return deleta_xml,erro_xml,erro_par_desconhecido,resultados,erro_xml_desconhecido