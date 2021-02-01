def analisa_cruzamento_dados(lista,dicionario):
    erro_xml_desconhecido = False
    erro_xml = []
    resultados = {}
    erro_par_desconhecido = False

    for leitura_no_pdf in range(0,len(lista)):
      erros = False
      for leitura_no_aprovado in range(0,len(dicionario.keys())):
        if dicionario[leitura_no_aprovado][1] == False:
          if lista[leitura_no_pdf] == dicionario[leitura_no_aprovado][0][0:44]:
            dicionario[leitura_no_aprovado] = dicionario[leitura_no_aprovado][0], True
            resultados[leitura_no_pdf] = lista[leitura_no_pdf],dicionario[leitura_no_aprovado][0]
            erros = False
            break
          if ((lista[leitura_no_pdf]) != (dicionario[leitura_no_aprovado][0][0:44])):
            if dicionario[leitura_no_aprovado][1] != "88888888888888888888888888888888888888888888": 
              resultados[leitura_no_pdf] = lista[leitura_no_pdf],"Par Não Encontrado"
              erros = True
        else:
            continue
      if (erros  == True):
        if (lista[leitura_no_pdf] == "88888888888888888888888888888888888888888888"):
          erros = False
        else:
          erro_xml.append(lista[leitura_no_pdf])
          erro_par_desconhecido = True
    
    deleta_xml = []
    for leitura_no_aprovado in range(0,len(dicionario.keys())):
      if dicionario[leitura_no_aprovado][1] == False:
        if dicionario[leitura_no_aprovado][0] != "99999999999999999999999999999999999999999999":
          erro_xml_desconhecido = True
          deleta_xml.append(dicionario[leitura_no_aprovado][0])

    return deleta_xml,erro_xml,erro_par_desconhecido,resultados,erro_xml_desconhecido