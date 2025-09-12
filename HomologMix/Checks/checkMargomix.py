import os

def checkMargomix():
    margomixPath = '/Margomix/Margomix.ini'
    return os.path.exists(margomixPath)

