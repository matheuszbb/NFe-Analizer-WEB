def busca_dados(os,extract_text,PyPDF4):
    def analisa_pdf(os,extract_text,PyPDF4):  
        try: 
            arquivo = open(os.path.expanduser('~')+"/Desktop/RelLivroFiscalSaidaNFCe.pdf", "rb")

            linha = PyPDF4.PdfFileReader(arquivo)
            numero_de_paginas = linha.getNumPages()

            l=""
            lista = []

            pagina_test = linha.getPage(0)
            pdf_test = pagina_test.extractText()

            if "Id NFC-e:" in pdf_test:
                for n in range(0,numero_de_paginas):
                    pagina = linha.getPage(n)
                    pdf = pagina.extractText()
                    for m in pdf:
                        l=l+m
                        if m == '\n':
                            lista.append(l.replace('\n',""))
                            l=""
                lista_pdf = []

                for n in range(0,len(lista)):
                    if (lista[n] == "Id NFC-e:"):
                        lista_pdf.append(lista[n+1])
            else:
                arquivo = extract_text(os.path.expanduser('~')+"/Desktop/RelLivroFiscalSaidaNFCe.pdf")
                                    
                l=""
                lista = []
                
                for m in arquivo:
                    l=l+m
                    if m == '\n':
                        lista.append(l.replace('\n',""))
                        l=""
                
                lista_pdf = []
                            
                for n in range(0,len(lista)):
                    if (lista[n][:(54-45)] == "Id NFC-e:"):
                        lista_pdf.append(lista[n][(54-44):].replace(" ",""))

            return lista_pdf
        except:
            lista_pdf = False
            return lista_pdf

    def analisa_xml(os):
        try:
            lista_xml = []

            for xml in os.listdir(os.path.expanduser('~')+"/Desktop/Aprovada"):
                lista_xml.append(xml)

            return lista_xml
        except:
            lista_xml = False
            return lista_xml
    
    lista_pdf = analisa_pdf(os,extract_text,PyPDF4)
    if lista_pdf == False:
        lista_xml = True
        return lista_pdf,lista_xml

    lista_xml = analisa_xml(os) 
    if lista_xml == False:
        return lista_pdf,lista_xml

    return lista_pdf,lista_xml
