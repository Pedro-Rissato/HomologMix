import os

def checkRMM():
    rmmPath = '/Program Files/TacticalAgent'
    return os.path.exists(rmmPath)

print(checkRMM())