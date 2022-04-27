from library import clean
def askExit(c, na=None):
    if '-na' in na and '-c' in na:
        clean.clean(c)
        return False
    elif '-na' in na:
        return False
    elif '-c' in na:
        clean.clean(c)
        return False
    else:
        match input("\n• Are you sure you want to exit? (Y\\N)\n\t• ").lower():
            case "y":    
                return False
            case "n":
                return True
            case "yc":
                clean.clean(c)
                return False
            case default:
                print("Invalid answer, automatically exiting...")
                return False
    