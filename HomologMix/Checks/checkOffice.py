'''
Função para checar se tem o Office 2010 instalado na máquina
Busca no diretório padrão
retorna True se estiver lá e False caso não esteja
'''

import os

def checkOffice():
    officePath = '/ProgramData/Microsoft/Windows/Start Menu/Programs/Microsoft Office/Microsoft Outlook 2010.lnk'
    return os.path.exists(officePath)

