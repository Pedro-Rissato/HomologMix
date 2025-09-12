import os

def checkPXdoc():
    pxdocPath = os.path.join(os.environ['USERPROFILE'],'Documents', 'Polimix')
    return os.path.exists(pxdocPath)

