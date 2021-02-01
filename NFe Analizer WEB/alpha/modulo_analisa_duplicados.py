def analisa_duplicados(lista):
    lista_duplicados = []
    duplicado = False
    for verifica_lista in range(0,len(lista)):
      erros = 0
      for verifica_lista_duplicado in range(0,len(lista)):
        if ((lista[verifica_lista]) == (lista[verifica_lista_duplicado])):
          erros = erros + 1
      if (erros >= 2):
        if lista[verifica_lista] not in lista_duplicados:
            lista_duplicados.append(lista[verifica_lista])
        duplicado = True

    return lista_duplicados,duplicado 