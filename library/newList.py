def returnNewList(lt):
    x=""
    for item in lt:
        x += f"'{item}', "
    x = x[0:len(x)-2]
    return x