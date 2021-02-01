def analisa_tamanho(lista,dicionario):
  tamanho_lista = len(lista)
  tamanho_dicionario = len(dicionario.keys())

  if (tamanho_lista > tamanho_dicionario):
    while(len(lista) != len(dicionario.keys())):
      dicionario[len(dicionario.keys())] = "99999999999999999999999999999999999999999999",False
  else:
    while(len(dicionario.keys()) != len(lista)):
      lista.append("88888888888888888888888888888888888888888888")

  return lista,dicionario
    

