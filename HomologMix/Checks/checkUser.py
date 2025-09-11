'''
checkUser = Polimix
'''

from pathlib import Path

def check_User():
    User = Path.home().name.upper()
    if User == "POLIMIX":
        return True
    else:
        return False, User
