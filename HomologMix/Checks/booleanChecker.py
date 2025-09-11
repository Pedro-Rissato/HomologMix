from checkUser import check_User
from checkWinrar import checkWinrar
from checkOffice import checkOffice
from checkJava import checkJava

def function_checker():
    functions = {
        "Usuário": check_User,
        "Winrar": checkWinrar,
        "Office": checkOffice,
        "Java": checkJava,
    }
    falses = []
    for name, func in functions.items():
        try:
            resultado = func()

            # Caso seja tupla (True/False, extra_info)
            if isinstance(resultado, tuple):
                status, info = resultado
                if not status:
                    falses.append(f"{name} → INCORRETO (Usuário detectado: {info} \n )")

            # Caso seja só True/False
            else:
                if not resultado:
                    falses.append(f"{name} → INCORRETO")

        except Exception as e:
            falses.append(f"{name} (erro: {e})")
    return falses
print("User:", check_User())
print("Winrar:", checkWinrar())
print("Office:", checkOffice())
print("Java:", checkJava())
