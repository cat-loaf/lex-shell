from library import clean
def askExit(c, na=None):
    if na == None:
        match input("\n• Are you sure you want to exit? (Y\\N)\n\t• ").lower():
            case "y":    
                return False
            case "n":
                return True
            case "yc":
                clean.clean(c)
            case default:
                print("Invalid answer, automatically exiting...")
    elif na == '-na' or na == "-n":
        return False