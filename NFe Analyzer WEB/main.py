import os
from modulo_back_end import back_end

diretorio = os.path.expanduser('~')+"/Documents/NFe Analyzer WEB"
if "confirmado.txt" in os.listdir(diretorio):
    back_end()
else:
    os.system("pip install PyPDF4")
    os.system("pip install pdfminer.six")
    os.system("pip install flask")
    confirmado = open(os.path.expanduser('~')+"/Documents/NFe Analyzer WEB/confirmado.txt","w")
    confirmado.close()
    back_end()