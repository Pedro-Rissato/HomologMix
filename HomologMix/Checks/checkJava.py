'''
Função para checar se tem o Java instalado na máquina
Busca no diretório padrão
retorna True se estiver lá e False caso não esteja
'''

import os

def checkJava():
    javaPath = '/Program Files (x86)/Java/jre1.8.0_461'
    return os.path.exists(javaPath)

