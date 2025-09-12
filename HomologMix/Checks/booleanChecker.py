from checkUser import check_User
from checkWinrar import checkWinrar
from checkOffice import checkOffice
from checkJava import checkJava
from checkPXdoc import checkPXdoc
from checkGed import checkGed
from checkGedoc import checkGedoc
from checkRMM import checkRMM
from checkBitDefender import checkBitDefender
from checkMargomix import checkMargomix


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
print("User:", check_User())
print("Winrar:", checkWinrar())
print("Office:", checkOffice())
print("Java:", checkJava())
