from HomologMix.old_checks.checkUser import check_User
from HomologMix.old_checks.checkWinrar import checkWinrar
from HomologMix.old_checks.checkOffice import checkOffice
from HomologMix.old_checks.checkJava import checkJava
from HomologMix.old_checks.checkPXdoc import checkPXdoc
from HomologMix.old_checks.checkGed import checkGed
from HomologMix.old_checks.checkGedoc import checkGedoc
from HomologMix.old_checks.checkRMM import checkRMM
from checkBitDefender import checkBitDefender
from HomologMix.old_checks.checkMargomix import checkMargomix


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
