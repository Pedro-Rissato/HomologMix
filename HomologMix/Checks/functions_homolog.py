import os
from pathlib import Path

def checkBitDefender():
    BDpath = '/Program Files/Bitdefender'
    return os.path.exists(BDpath)

def checkMargomix():
    margomixPath = '/Margomix/Margomix.ini'
    return os.path.exists(margomixPath)

def checkPXdoc():
    pxdocPath = os.path.join(os.environ['USERPROFILE'],'Documents', 'Polimix')
    return os.path.exists(pxdocPath)

def checkGed():
    gedPath = '/Ged/GedocSync/app/DatabaseGenerator.log'
    return os.path.exists(gedPath)

def homolog_check():
    functions = {
        "Usuário": check_User,
        "Winrar": checkWinrar,
        "Office": checkOffice,
        "Java": checkJava,
        "Ged": checkGed,
        "Gedoc": checkGedoc,
        "Pasta Polimix": checkPXdoc,
        "RMM": checkRMM,
        "BitDefender": checkBitDefender,
        "Margomix": checkMargomix,




    }
    falses = []
    for name, func in functions.items():
        try:
            resultado = func()

            # Caso seja tupla (True/False, extra_info)
            if isinstance(resultado, tuple):
                status, info = resultado
                if not status:
                    falses.append(f"{name} → INCORRETO (Usuário detectado: {info})\n\n Será necessário criar um usuário com o nome Polimix!\n")

            # Caso seja só True/False
            else:
                if not resultado:
                    falses.append(f"{name} → NÃO INSTALADO")

        except Exception as e:
            falses.append(f"{name} (erro: {e})")
    return falses

def checkRMM():
    rmmPath = '/Program Files/TacticalAgent'
    return os.path.exists(rmmPath)

def checkGedoc():
    gedocPath = '/GedocFlexUpdater/app/work'
    return os.path.exists(gedocPath)

def checkWinrar():
    winrarPath = '/Program Files/WinRAR'
    return os.path.exists(winrarPath)

def check_User():
    User = Path.home().name.upper()
    if User == "POLIMIX":
        return True
    else:
        return False, User

def checkOffice():
    officePath = '/ProgramData/Microsoft/Windows/Start Menu/Programs/Microsoft Office/Microsoft Outlook 2010.lnk'
    return os.path.exists(officePath)

def checkJava():
    javaPath = '/Program Files (x86)/Java/jre1.8.0_461'
    return os.path.exists(javaPath)
