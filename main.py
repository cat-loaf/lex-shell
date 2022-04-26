from win10toast import ToastNotifier

from library import clean, exit, restart, version, newList
from platform import system
import os, time

def main():
    clearCommand = "cls" if system().lower() == "windows" else "clear"
    t = ToastNotifier()
    try:
        run = True
        clean.clean(clearCommand)
        print(r"lex-shell { version: "+version.getVersion()+r" }")
        while run:
            origState = input("> ")
            listState = origState.split(" ")
            statement = origState.lower().split(" ")
            match statement[0]:
                case "quit" | "exit" | "exit()" | "quit()":
                    run = exit.askExit(clearCommand)
                    
                case "clear" | "cls" | "clean":
                    clean.clean(clearCommand)
                
                case "restart":
                    print(f"Restarting...")
                    time.sleep(0.25)
                    
                    restart.restart()
                case "version" | "ver":
                    print(version.getVersion()) 
                    
                case default:
                    if len(listState) != 1: # create a class that extends list, with custom repr
                        print(newList.returnNewList(listState)+" is not a valid command.\n\t")
                    else:
                        print("'"+listState[0] + "' is not a valid command.\n")
                    
    except KeyboardInterrupt:
        if exit.askExit(clearCommand) == True:
            main()
            
if __name__ == '__main__':
    main()