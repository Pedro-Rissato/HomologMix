import os

def checkGed():
    gedPath = '/Ged/GedocSync/app/DatabaseGenerator.log'
    return os.path.exists(gedPath)

print(checkGed())