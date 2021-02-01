def limpeza(deleta_xml,os):
    getUser = lambda: os.environ["USERNAME"] if "C:" in os.getcwd() else os.environ["USER"]
    usuario_pc = getUser()
    
    for x in deleta_xml:
        for xml in os.listdir("C:/Users/"+usuario_pc+"/Desktop/Aprovada"):
            if (xml == x):
              os.remove("C:/Users/"+usuario_pc+"/Desktop/Aprovada/" + xml)
