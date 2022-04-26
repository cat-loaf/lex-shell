from library import clean
def askExit(c):
    match input("• Are you sure you want to exit? (Y\\N)\n\t• ").lower():
        case "y":
            return False
        case "n":
            return True
        case "yc":
            clean.clean(c)
        case default:
            print("Invalid answer, automatically exiting...")
      