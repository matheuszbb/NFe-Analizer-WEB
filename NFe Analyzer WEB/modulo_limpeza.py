def limpeza(os):
    deleta_xml = []

    deleta = open(os.path.expanduser("~")+"/Documents/NFe Analyzer WEB/deleta_xml.txt","r")
    
    for y in deleta:
        deleta_xml.append(y.replace("\n",""))
    
    deleta.close()

    for x in deleta_xml:
        for xml in os.listdir(os.path.expanduser('~')+"/Desktop/Aprovada"):
            if (xml == x):
              os.remove(os.path.expanduser('~')+"/Desktop/Aprovada/" + xml)
