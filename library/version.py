import os
def getVersion():
    createVersionFileCheck()
    f = open("library\\version", "r")
    ver = int(f.readline())
    f.close()
    return f"Version: {str(ver)}"
def updateVersion():
    createVersionFileCheck()
    f = open("library\\version", "r")
    version = int(f.readline())
    version += 1
    f = open("library\\version", "w")
    f.write(str(version))
    f.close()

def setVersion(ver: int):
    try:
        createVersionFileCheck()
        int(ver)
        f = open("library\\version", "w").write(str(ver))
    except ValueError:
        print("Please provide an integer")
        
def createVersionFileCheck():
    try:
        f = open("library\\version", "r+")
        f.readline()
        if f == "":
            b = open("library\\version", "w")
            b.write("0")
            b.close()
        f.close()
    except FileNotFoundError:
        os.system("echo 0 > library\\version")