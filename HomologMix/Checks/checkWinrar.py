'''
Função para checar se tem o Winrar instalado na máquina
Busca no diretório padrão
retorna True se estiver lá e False caso não esteja
'''

import os

def checkWinrar():
    winrarPath = '/Program Files/WinRAR'
    return os.path.exists(winrarPath)




