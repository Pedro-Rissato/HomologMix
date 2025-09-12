import os

def checkBitDefender():
    BDpath = '/Program Files/Bitdefender'
    return os.path.exists(BDpath)

print(checkBitDefender())