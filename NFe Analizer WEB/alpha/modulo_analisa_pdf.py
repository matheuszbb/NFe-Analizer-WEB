def analisa_pdf(os,PyPDF4):    
  getUser = lambda: os.environ["USERNAME"] if "C:" in os.getcwd() else os.environ["USER"]
  usuario_pc = getUser()

  arquivo = open("C:/Users/"+usuario_pc+"/Desktop/RelLivroFiscalSaidaNFCe.pdf", "rb")

  linha = PyPDF4.PdfFileReader(arquivo)
  numero_de_paginas = linha.getNumPages()

  l=""
  lista_pdf = []

  for n in range(0,numero_de_paginas):
    pagina = linha.getPage(n)
    pdf = pagina.extractText()
    for m in pdf:
      l=l+m
      if m == '\n':
        lista_pdf.append(l.replace('\n',""))
        l=""
  
  lista = []

  for n in range(0,len(lista_pdf)):
    if (lista_pdf[n] == "Id NFC-e:"):
      lista.append(lista_pdf[n+1])

  lista.append("27200705329907000112650010000050121805275456")

  return lista