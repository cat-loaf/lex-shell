from win10toast import ToastNotifier
#from library.clean import clean
#from library.exit import askExit
from library import clean
from library import exit
from platform import system
import os
def main():
    clearCommand = "cls" if system().lower() == "windows" else "clear"
    t = ToastNotifier()
    try:
        run = True
        while run:
            origState = input("> ")
            listState = origState.split(" ")
            statement = origState.lower().split(" ")
            match statement[0]:
                case "quit" | "exit" | "exit()" | "quit()":
                    run = exit.askExit(clearCommand)
                    
                case "clear" | "cls" | "clean":
                    clean.clean(clearCommand)
                    
                case default:
                    if len(listState) != 1: # create a class that extends list, with custom repr
                        print(str(listState)+" is not a valid command.\n\t")
                    else:
                        print("'"+listState[0] + "' is not a valid command.\n")
                    
    except KeyboardInterrupt:
        if exit.askExit(clearCommand) == True:
            main()
            
if __name__ == '__main__':
    main()