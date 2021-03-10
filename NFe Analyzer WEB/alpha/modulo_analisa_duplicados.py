def analisa_duplicados(lista_pdf):
  lista_duplicados = []
  duplicado = False

  for verifica_lista in lista_pdf:
    if lista_pdf.count(verifica_lista) >= 2:
      if verifica_lista not in lista_duplicados:
        lista_duplicados.append(verifica_lista)
        duplicado = True

  return lista_duplicados,duplicado 