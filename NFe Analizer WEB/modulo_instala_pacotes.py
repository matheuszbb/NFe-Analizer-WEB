def instala_pacotes(os,webbrowser):
    diretorio = os.path.expanduser('~')+"/Documents/NFe Analizer WEB"
    if "confirmado.txt" in os.listdir(diretorio):
        webbrowser.open_new_tab('http://127.0.0.1:5000')
    else:
        os.system("pip install --upgrade pip")
        os.system("pip install pypdf4")
        os.system("pip install flask")
        confirmado = open(os.path.expanduser('~')+'/Documents/NFe Analizer WEB/confirmado.txt',"w")
        confirmado.close()
        webbrowser.open_new_tab('http://127.0.0.1:5000')