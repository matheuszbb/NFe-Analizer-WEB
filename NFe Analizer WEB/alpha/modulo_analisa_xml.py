def analisa_xml(os):
    getUser = lambda: os.environ["USERNAME"] if "C:" in os.getcwd() else os.environ["USER"]
    usuario_pc = getUser()

    dicionario = {}
    cont = 0

    for xml in os.listdir("C:/Users/"+usuario_pc+"/Desktop/Aprovada"):
        dicionario[cont] = xml,False
        cont = cont + 1
    
    return dicionario