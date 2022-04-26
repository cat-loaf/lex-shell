def getVersion():
    f = open("library\\version", "r")
    ver = int(f.readline())
    return (f"Version: {ver}")

def updateVersion():
    f = open("library\\version", "r")
    version = int(f.readline())
    version += 1
    f = open("library\\version", "w")
    f.write(str(version))
    f.close()

def setVersion(ver: int):
    try:
        int(ver)
        f = open("library\\version", "w").write(str(ver))
    except ValueError:
        print("Please provide an integer")
    