def limpeza(deleta_xml,os):
    for x in deleta_xml:
        for xml in os.listdir(os.path.expanduser('~')+"/Desktop/Aprovada"):
            if (xml == x):
              os.remove(os.path.expanduser('~')+"/Desktop/Aprovada/" + xml)
